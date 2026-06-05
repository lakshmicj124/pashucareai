import os
import cv2
import hashlib
from pathlib import Path

COW_DATASET_DIR = Path(r"c:\Users\DELL\Documents\cow disease project\dataset\cow")

def get_image_md5(img_path):
    try:
        img = cv2.imread(str(img_path))
        if img is None:
            return None
        # Resize to static shape and compute hash to catch resized duplicates
        img_resized = cv2.resize(img, (32, 32))
        return hashlib.md5(img_resized.tobytes()).hexdigest()
    except Exception:
        return None

def validate_dataset():
    print("==========================================")
    print("      COW DATASET VALIDATION REPORT       ")
    print("==========================================\n")
    
    expected_folders = [
        "healthy",
        "lumpy_skin_disease",
        "mastitis",
        "foot_and_mouth_disease",
        "ringworm",
        "black_quarter",
        "theileriosis"
    ]
    
    empty_folders = []
    corrupted_images = []
    valid_counts = {}
    md5_dict = {}
    duplicates = []
    
    img_extensions = {".jpg", ".jpeg", ".png", ".webp", ".jfif"}
    
    for folder in expected_folders:
        folder_path = COW_DATASET_DIR / folder
        if not folder_path.exists():
            print(f"[ERROR] Missing expected class directory: {folder}")
            empty_folders.append(folder)
            valid_counts[folder] = 0
            continue
            
        files = [f for f in folder_path.glob("**/*") if f.suffix.lower() in img_extensions]
        if not files:
            empty_folders.append(folder)
            valid_counts[folder] = 0
            print(f"[WARN] Class '{folder}' is EMPTY.")
            continue
            
        print(f"Scanning Class '{folder}' ({len(files)} files found)...")
        valid_img_count = 0
        for f in files:
            # 1. Check for corruption
            try:
                img = cv2.imread(str(f))
                if img is None:
                    corrupted_images.append(str(f))
                    continue
            except Exception:
                corrupted_images.append(str(f))
                continue
                
            valid_img_count += 1
            
            # 2. Check duplicates
            h = get_image_md5(f)
            if h:
                if h in md5_dict:
                    duplicates.append((str(f), md5_dict[h]))
                else:
                    md5_dict[h] = str(f)
                    
        valid_counts[folder] = valid_img_count

    print("\n--- RESULTS SUMMARY ---")
    print("Class Counts (Valid Images):")
    for cls, count in valid_counts.items():
        print(f"  {cls}: {count}")
        
    print(f"\nEmpty Classes: {len(empty_folders)}")
    for f in empty_folders:
        print(f"  - {f}")
        
    print(f"\nCorrupted Images: {len(corrupted_images)}")
    for f in corrupted_images:
        print(f"  - {f}")
        
    print(f"\nDuplicate Images: {len(duplicates)}")
    if duplicates:
        print("  Showing first 10 duplicates:")
        for dup, orig in duplicates[:10]:
            print(f"  - {os.path.basename(dup)} is a duplicate of {os.path.basename(orig)}")
            
    print("==========================================")

if __name__ == "__main__":
    validate_dataset()
