import os
import shutil
from pathlib import Path

DATASET_DIR = Path(r"c:\Users\DELL\Documents\cow disease project\dataset")

def move_dir(src_name, dest_path):
    src = DATASET_DIR / src_name
    dest = DATASET_DIR / dest_path
    if src.exists():
        print(f"Moving {src_name} to {dest_path}...")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            # If destination already exists, merge contents
            for item in src.iterdir():
                shutil.move(str(item), str(dest / item.name))
            shutil.rmtree(str(src))
        else:
            shutil.move(str(src), str(dest))
    else:
        print(f"Source folder not found: {src_name}")

def reorganize():
    print("Starting dataset reorganization...")
    
    # 1. Cow reorganization
    move_dir("healthy", "cow/healthy")
    move_dir("lumpy", "cow/lumpy_skin")
    move_dir("foot-and-mouth", "cow/foot_and_mouth")
    (DATASET_DIR / "cow/mastitis").mkdir(parents=True, exist_ok=True)
    
    # 2. Sheep reorganization
    move_dir("sheep_pox", "sheep/sheep_pox")
    move_dir("foot_rot", "sheep/foot_rot")
    move_dir("bluetongue", "sheep/bluetongue")
    move_dir("diseased sheep", "sheep/diseased_sheep")
    move_dir("ringworm", "sheep/ringworm")
    
    # 3. Clean up extra mange folder if not empty
    mange_src = DATASET_DIR / "mange"
    if mange_src.exists():
        # Move to sheep/mange
        move_dir("mange", "sheep/mange")
        
    # 4. Handle sheep healthy folder
    sheep_healthy_dir = DATASET_DIR / "sheep/healthy"
    sheep_healthy_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy healthy goat images as healthy sheep images (both small ruminants) to avoid using cow images
    goat_healthy_dir = DATASET_DIR / "goat/healthy"
    if goat_healthy_dir.exists():
        print("Populating sheep/healthy with healthy goat images as templates...")
        for img_file in goat_healthy_dir.glob("*"):
            if img_file.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp", ".jfif"]:
                shutil.copy(str(img_file), str(sheep_healthy_dir / f"sheep_{img_file.name}"))
                
    print("Dataset reorganization complete!")

if __name__ == "__main__":
    reorganize()
