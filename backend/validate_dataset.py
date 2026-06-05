import os
import cv2
import hashlib
from pathlib import Path

DATASET_DIR = Path(r"c:\Users\DELL\Documents\cow disease project\dataset")

def get_image_hash(img_path):
    """Calculate MD5 hash of image pixels to detect exact duplicates."""
    try:
        img = cv2.imread(str(img_path))
        if img is None:
            return None
        # Convert to grayscale and resize to standard small size for fast comparison
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (16, 16))
        return hashlib.md5(resized.tobytes()).hexdigest()
    except Exception:
        return None

def validate():
    print("==========================================")
    print("       DATASET VALIDATION REPORT          ")
    print("==========================================")
    
    img_extensions = {".jpg", ".jpeg", ".png", ".webp", ".jfif"}
    corrupt_images = []
    hashes = {}
    duplicates = []
    
    categories = ["cow", "goat", "sheep"]
    
    for category in categories:
        cat_dir = DATASET_DIR / category
        if not cat_dir.exists():
            print(f"[WARN] Category directory not found: {cat_dir}")
            continue
            
        print(f"\nValidating category: {category}")
        for class_dir in cat_dir.iterdir():
            if not class_dir.is_dir():
                continue
                
            class_name = class_dir.name
            files = list(class_dir.glob("*"))
            img_files = [f for f in files if f.suffix.lower() in img_extensions]
            
            print(f"  Class '{class_name}': {len(img_files)} images found.")
            
            for img_path in img_files:
                # 1. Check corruption
                try:
                    img = cv2.imread(str(img_path))
                    if img is None or img.size == 0:
                        corrupt_images.append(img_path)
                        continue
                except Exception:
                    corrupt_images.append(img_path)
                    continue
                    
                # 2. Check duplicates
                h = get_image_hash(img_path)
                if h is not None:
                    if h in hashes:
                        duplicates.append((img_path, hashes[h]))
                    else:
                        hashes[h] = img_path
                        
                # 3. Check for disease image leaked into healthy (based on filename heuristic)
                if class_name == "healthy":
                    fn_lower = img_path.name.lower()
                    diseased_keywords = ["lumpy", "pox", "mange", "orf", "ppr", "bluetongue", "foot", "rot", "scab", "ringworm", "lesion", "diseased"]
                    if any(kw in fn_lower for kw in diseased_keywords):
                        print(f"    [ALERT] Possible diseased image inside healthy folder: {img_path.name}")
                        
    print("\n=================== SUMMARY ===================")
    print(f"Corrupt Images found: {len(corrupt_images)}")
    for f in corrupt_images:
        print(f"  - {f}")
        
    print(f"Duplicate Images found: {len(duplicates)}")
    for f, orig in duplicates[:10]:
        print(f"  - {f.name} is duplicate of {orig.name}")
    if len(duplicates) > 10:
        print(f"  ... and {len(duplicates) - 10} more.")
        
    print("===============================================")
    
    return len(corrupt_images) == 0 and len(duplicates) == 0

if __name__ == "__main__":
    validate()
