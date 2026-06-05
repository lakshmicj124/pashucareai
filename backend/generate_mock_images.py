import os
import cv2
import numpy as np

DATASET_DIR = r"c:\Users\DELL\Documents\cow disease project\dataset"

classes = ["sheep_pox", "orf", "foot_rot", "bluetongue", "ringworm", "mange"]

for cls in classes:
    folder = os.path.join(DATASET_DIR, cls)
    os.makedirs(folder, exist_ok=True)
    for i in range(10):
        # Create a mock image with random noise, adding a unique color cast per class to help the model learn
        img = np.random.randint(0, 255, (64, 64, 3), dtype=np.uint8)
        if cls == "sheep_pox": img[:,:,0] = 200
        elif cls == "orf": img[:,:,1] = 200
        elif cls == "foot_rot": img[:,:,2] = 200
        elif cls == "bluetongue": img[:,:,0] = 100; img[:,:,1] = 100
        elif cls == "ringworm": img[:,:,1] = 100; img[:,:,2] = 100
        elif cls == "mange": img[:,:,0] = 100; img[:,:,2] = 100
        cv2.imwrite(os.path.join(folder, f"mock_{i}.jpg"), img)

print("Mock dataset generated.")
