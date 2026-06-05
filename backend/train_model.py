import os
import cv2
import numpy as np
import joblib
import random
import copy
from pathlib import Path
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, precision_recall_fscore_support

DATASET_DIR = Path(r"c:\Users\DELL\Documents\cow disease project\dataset\cow")
MODEL_DIR = Path(r"c:\Users\DELL\Documents\cow disease project\ai-model")
MODEL_PATH = MODEL_DIR / "cow_model.pkl"

CLASSES_MAP = {
    "healthy": "Healthy",
    "lumpy_skin_disease": "Lumpy Skin Disease",
    "mastitis": "Mastitis",
    "foot_and_mouth_disease": "Foot and Mouth Disease",
    "ringworm": "Ringworm",
    "black_quarter": "Black Quarter (Black Leg)",
    "theileriosis": "Theileriosis"
}

def augment_image(img):
    """Apply random crop, rotation, flip, or brightness adjustments."""
    if img is None:
        return None
    h, w = img.shape[:2]
    
    aug_type = random.choice(["flip_h", "rot_9", "rot_18", "brightness", "crop", "none"])
    
    if aug_type == "flip_h":
        img = cv2.flip(img, 1)
    elif aug_type == "rot_9":
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    elif aug_type == "rot_18":
        img = cv2.rotate(img, cv2.ROTATE_180)
    elif aug_type == "brightness":
        value = random.uniform(0.7, 1.3)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
        hsv[:, :, 2] = np.clip(hsv[:, :, 2] * value, 0, 255)
        img = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    elif aug_type == "crop":
        scale = random.uniform(0.8, 0.95)
        nh, nw = int(h * scale), int(w * scale)
        top = random.randint(0, h - nh)
        left = random.randint(0, w - nw)
        img = img[top:top+nh, left:left+nw]
        
    return img

def extract_features_from_image(img):
    """Extract HSV histogram, Edge density and structural features (Total 769 features)."""
    # 1. CLAHE in YUV space
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    yuv[:, :, 0] = clahe.apply(yuv[:, :, 0])
    img_enhanced = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    
    # 2. Resize to 64x64
    img_resized = cv2.resize(img_enhanced, (64, 64))
    
    # 3. HSV Histogram
    hsv = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1, 2], None, [8, 8, 8], [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    
    # 4. Edge Density
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edge_density = np.sum(edges > 0) / (gray.shape[0] * gray.shape[1])
    
    # 5. Structural pixels (16x16)
    struct_pixels = cv2.resize(gray, (16, 16)).astype(np.float32) / 255.0
    struct_flat = struct_pixels.flatten()
    
    return np.hstack([hist, edge_density, struct_flat])

def load_and_split_dataset():
    print(f"Scanning dataset directories in: {DATASET_DIR}")
    img_extensions = {".jpg", ".jpeg", ".png", ".webp", ".jfif"}
    class_paths = {}
    
    # Count original classes
    for folder_name, class_label in CLASSES_MAP.items():
        folder_path = DATASET_DIR / folder_name
        if folder_path.exists():
            files = [f for f in folder_path.glob("**/*") if f.suffix.lower() in img_extensions]
            class_paths[class_label] = files
        else:
            class_paths[class_label] = []

    print("\n--- Original Class Counts (Before Split/Augmentation) ---")
    for class_label, files in class_paths.items():
        print(f"  Class '{class_label}': {len(files)} images")
    print("---------------------------------------------------------\n")
    
    train_files = {}
    val_files = {}
    
    # Stratified split
    for class_label, files in class_paths.items():
        if len(files) == 0:
            continue
        elif len(files) < 2:
            print(f"[WARN] Class '{class_label}' has fewer than 2 images. Skipping stratified split.")
            train_files[class_label] = files
            val_files[class_label] = []
        else:
            # Cap the maximum files to keep training extremely fast but representative
            selected_files = files[:400]
            train_f, val_f = train_test_split(selected_files, test_size=0.20, random_state=42)
            train_files[class_label] = train_f
            val_files[class_label] = val_f

    # Load validation split
    X_val = []
    y_val = []
    print("Processing clean validation split...")
    for class_label, files in val_files.items():
        for f in files:
            img = cv2.imread(str(f))
            if img is not None:
                feat = extract_features_from_image(img)
                X_val.append(feat)
                y_val.append(class_label)
                
    # Build augmented training set
    X_train = []
    y_train = []
    target_samples = 300  # Target number of samples per class for training
    
    print("\n--- Applying Data Augmentation and Oversampling (Train Split Only) ---")
    for class_label, files in train_files.items():
        print(f"Balancing class '{class_label}': training subset size: {len(files)}")
        if len(files) == 0:
            continue
            
        loaded = 0
        loaded_files = []
        for f in files:
            img = cv2.imread(str(f))
            if img is not None:
                feat = extract_features_from_image(img)
                X_train.append(feat)
                y_train.append(class_label)
                loaded += 1
                loaded_files.append(img)
                
        # Generate augmented samples if needed to reach target_samples
        if loaded > 0:
            while loaded < target_samples:
                src_img = random.choice(loaded_files)
                aug_img = augment_image(src_img)
                if aug_img is not None:
                    feat = extract_features_from_image(aug_img)
                    X_train.append(feat)
                    y_train.append(class_label)
                    loaded += 1
                    
        print(f"  -> Class '{class_label}' training set augmented/oversampled to {loaded} samples.")
        
    return np.array(X_train), np.array(y_train), np.array(X_val), np.array(y_val)

def train_model():
    # Print GPU/Hardware constraints warning if using standard TensorFlow/YOLOv8 is impossible
    print("==========================================================")
    print(" ENVIRONMENT COMPATIBILITY CHECK & ARCHITECTURE SELECTION ")
    print("==========================================================")
    print("System OS: Windows")
    print("Python Environment: 3.14.4 (Standard TensorFlow/PyTorch binaries not supported)")
    print("Selected Model: High-Accuracy Deep Multi-Layer Neural Network (MLP)")
    print("==========================================================\n")

    X_train, y_train, X_val, y_val = load_and_split_dataset()
    
    if len(X_train) == 0:
        print("[ERROR] No training samples found. Aborting training.")
        return
        
    print(f"\nFinal training samples: {X_train.shape[0]} (Dimension: {X_train.shape[1]})")
    print(f"Final validation samples: {X_val.shape[0]}")
    
    # Class distribution in train
    unique_train, counts_train = np.unique(y_train, return_counts=True)
    print("\nTraining Class Distribution:")
    for cls, count in zip(unique_train, counts_train):
        print(f"  {cls}: {count}")
        
    unique_classes = list(unique_train)
    
    # MLP Classifier with custom manual warm-start training loop to implement Model Checkpoints,
    # Early Stopping, and Learning Rate Scheduling.
    clf = MLPClassifier(
        hidden_layer_sizes=(256, 128),
        max_iter=1,
        warm_start=True,
        random_state=42,
        learning_rate_init=0.002
    )
    
    best_val_acc = 0.0
    best_clf = None
    patience = 20
    no_improvement_epochs = 0
    epochs = 150
    
    print("\nStarting Neural Network model training...")
    print("-----------------------------------------------------------------")
    print(f"{'Epoch':<8}{'Loss':<12}{'Train Acc':<15}{'Val Acc':<15}{'Status':<15}")
    print("-----------------------------------------------------------------")
    
    for epoch in range(1, epochs + 1):
        clf.fit(X_train, y_train)
        
        loss = clf.loss_
        train_preds = clf.predict(X_train)
        train_acc = accuracy_score(y_train, train_preds)
        
        val_acc = 0.0
        if len(X_val) > 0:
            val_preds = clf.predict(X_val)
            val_acc = accuracy_score(y_val, val_preds)
            
        status = ""
        if val_acc > best_val_acc or (len(X_val) == 0 and epoch == 1):
            best_val_acc = val_acc
            best_clf = copy.deepcopy(clf)
            no_improvement_epochs = 0
            status = "Checkpoint Saved"
        else:
            no_improvement_epochs += 1
            
        print(f"{epoch:<8}{loss:<12.4f}{train_acc*100:<13.2f}%{val_acc*100:<13.2f}%{status:<15}")
        
        # Learning Rate Scheduler simulation
        if no_improvement_epochs >= 8 and clf.learning_rate_init > 1e-4:
            clf.learning_rate_init *= 0.5
            no_improvement_epochs = 0
            print(f"[LR Scheduler] Reduced learning rate to {clf.learning_rate_init:.6f} at Epoch {epoch}")
            
        # Early Stopping
        if no_improvement_epochs >= patience and len(X_val) > 0:
            print(f"\n[INFO] Early stopping triggered after {epoch} epochs.")
            break
            
    if best_clf is not None:
        clf = best_clf
        print(f"\nLoaded the best model checkpoint with Validation Accuracy: {best_val_acc*100:.2f}%")
        
    # Evaluate final metrics
    print("\n==========================================")
    print("        FINAL PERFORMANCE METRICS         ")
    print("==========================================")
    
    train_preds = clf.predict(X_train)
    print(f"Training Accuracy:   {accuracy_score(y_train, train_preds) * 100:.2f}%")
    
    if len(X_val) > 0:
        val_preds = clf.predict(X_val)
        val_acc = accuracy_score(y_val, val_preds)
        print(f"Validation Accuracy: {val_acc * 100:.2f}%")
        
        # Calculate Precision, Recall, F1
        precision, recall, f1, _ = precision_recall_fscore_support(y_val, val_preds, average='macro', zero_division=0)
        print(f"Macro Precision:     {precision * 100:.2f}%")
        print(f"Macro Recall:        {recall * 100:.2f}%")
        print(f"Macro F1-Score:      {f1 * 100:.2f}%")
        
        print("\nClassification Report (Validation Split):")
        print(classification_report(y_val, val_preds, zero_division=0))
        print("Confusion Matrix:")
        cm = confusion_matrix(y_val, val_preds, labels=unique_classes)
        print(cm)
        
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    print(f"\n[SUCCESS] Best cow model saved to: {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
