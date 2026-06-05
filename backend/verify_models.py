import os
import cv2
import numpy as np
import joblib
from pathlib import Path

DATASET_DIR = r"c:\Users\DELL\Documents\cow disease project\dataset"
MODEL_DIR = r"c:\Users\DELL\Documents\cow disease project\ai-model"

COW_MODEL_PATH = os.path.join(MODEL_DIR, "cow_model.pkl")
SHEEP_MODEL_PATH = os.path.join(MODEL_DIR, "sheep_model.pkl")
GOAT_MODEL_PATH = os.path.join(MODEL_DIR, "goat_model.pkl")

# Define classes and paths for Cow model
COW_CLASSES = {
    "foot-and-mouth": "Foot and Mouth Disease",
    "healthy": "Healthy",
    "lumpy": "Lumpy Skin Disease"
}

# Define classes and paths for Sheep model
SHEEP_CLASSES = {
    "bluetongue": "Bluetongue",
    "foot_rot": "Foot Rot",
    "healthy": "Healthy",
    "orf": "Orf (Contagious Ecthyma)",
    "ringworm": "Ringworm",
    "mange": "Sarcoptic Mange",
    "sheep_pox": "Sheep Pox",
    "diseased sheep": "Sheep Scab (Psoroptic Mange)"
}

# Define classes and paths for Goat model
GOAT_CLASSES = {
    "goat/healthy": "Healthy",
    "goat/mange": "Mange Dermatitis",
    "goat/ppr": "Peste des Petits Ruminants (PPR)",
    "goat/goat_pox": "Goat Pox",
    "goat/orf": "Contagious Ecthyma (Orf)"
}

def extract_cow_sheep_features(img_path):
    try:
        img = cv2.imread(str(img_path))
        if img is None:
            return None
        img = cv2.resize(img, (64, 64))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1, 2], None, [8, 8, 8], [0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        edge_density = np.sum(edges > 0) / (gray.shape[0] * gray.shape[1])
        features = np.hstack([hist, edge_density])
        return features
    except Exception:
        return None

def extract_goat_features(img_path):
    try:
        img = cv2.imread(str(img_path))
        if img is None:
            return None
        # 1. Contrast enhancement: YUV equalization on L/Y channel
        yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        yuv[:, :, 0] = clahe.apply(yuv[:, :, 0])
        img_enhanced = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        
        # 2. Resize
        img_resized = cv2.resize(img_enhanced, (64, 64))
        
        # 3. Normalize & Feature extraction
        # A. HSV Histogram
        hsv = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1, 2], None, [8, 8, 8], [0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        
        # B. Edge Density
        gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        edge_density = np.sum(edges > 0) / (gray.shape[0] * gray.shape[1])
        
        # C. Structure features (16x16 grayscale, normalized)
        struct_pixels = cv2.resize(gray, (16, 16)).astype(np.float32) / 255.0
        struct_flat = struct_pixels.flatten()
        
        # Combine: 512 + 1 + 256 = 769 features
        features = np.hstack([hist, edge_density, struct_flat])
        return features
    except Exception:
        return None

def verify_animal_model(model_path, animal_name, classes_dict):
    print(f"\n==========================================")
    print(f"VERIFYING {animal_name.upper()} MODEL")
    print(f"==========================================")
    
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}")
        return
        
    try:
        model = joblib.load(model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        return
        
    img_extensions = {".jpg", ".jpeg", ".png", ".webp", ".jfif"}
    
    print(f"{'Folder Class':<30} | {'Expected Disease':<30} | {'Predicted Disease':<30} | {'Conf':<5} | {'Status':<5}")
    print("-" * 115)
    
    total_checked = 0
    total_passed = 0
    
    for folder, expected_label in classes_dict.items():
        folder_path = Path(DATASET_DIR) / folder
        
        # Fallback if healthy folder has different names
        if not folder_path.exists() and folder == "healthy" and animal_name == "Cow":
            folder_path = Path(DATASET_DIR) / "healthy"
            
        if not folder_path.exists():
            print(f"{folder:<30} | Folder does not exist at {folder_path}!")
            continue
            
        all_files = list(folder_path.rglob("*"))
        img_files = [f for f in all_files if f.suffix.lower() in img_extensions]
        
        img_imgs_sample = img_files[:3]
        if not img_imgs_sample:  # test up to 3 images per class
            print(f"{folder:<30} | No images found in {folder_path}!")
            continue
            
        for i, img_path in enumerate(img_imgs_sample):
            if animal_name == "Goat":
                features = extract_goat_features(img_path)
            else:
                features = extract_cow_sheep_features(img_path)
                
            if features is None:
                continue
                
            total_checked += 1
            predicted = model.predict([features])[0]
            probs = model.predict_proba([features])[0]
            conf = int(np.max(probs) * 100)
            
            # Normalizing class names for comparison
            p_norm = predicted.lower().replace(" (orf)", "").replace(" (psoroptic mange)", "").replace(" (contagious ecthyma)", "").replace(" dermatitis", "").strip()
            e_norm = expected_label.lower().replace(" (orf)", "").replace(" (psoroptic mange)", "").replace(" (contagious ecthyma)", "").replace(" dermatitis", "").strip()
            
            # Match rules
            status = "PASS" if p_norm in e_norm or e_norm in p_norm else "FAIL"
            if status == "PASS":
                total_passed += 1
                
            print(f"{folder + f' (img_{i})':<30} | {expected_label:<30} | {predicted:<30} | {conf:<5}% | {status}")
            
    print("-" * 115)
    pass_rate = (total_passed / total_checked * 100) if total_checked > 0 else 0
    print(f"Result: {total_passed}/{total_checked} predictions correct. Pass Rate: {pass_rate:.2f}%")

def main():
    verify_animal_model(COW_MODEL_PATH, "Cow", COW_CLASSES)
    verify_animal_model(SHEEP_MODEL_PATH, "Sheep", SHEEP_CLASSES)
    verify_animal_model(GOAT_MODEL_PATH, "Goat", GOAT_CLASSES)

if __name__ == '__main__':
    main()
