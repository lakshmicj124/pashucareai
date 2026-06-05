import os
from duckduckgo_search import DDGS
import requests

DATASET_DIR = r"c:\Users\DELL\Documents\cow disease project\dataset"

queries = {
    "sheep_pox": "sheep pox lesions sheep",
    "orf": "orf disease sheep mouth lesions",
    "foot_rot": "foot rot sheep hoof infection",
    "bluetongue": "bluetongue sheep swollen face",
    "ringworm": "ringworm sheep skin lesions",
    "mange": "sarcoptic mange sheep"
}

def download_images():
    ddgs = DDGS()
    for disease_folder, query in queries.items():
        folder_path = os.path.join(DATASET_DIR, disease_folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Downloading images for {disease_folder} into {folder_path}...")
        
        try:
            results = ddgs.images(query, max_results=15)
            count = 0
            for i, result in enumerate(results):
                try:
                    img_url = result['image']
                    response = requests.get(img_url, timeout=5)
                    if response.status_code == 200:
                        file_path = os.path.join(folder_path, f"img_{count}.jpg")
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                        print(f"  Saved {file_path}")
                        count += 1
                        if count >= 10:
                            break
                except Exception as e:
                    print(f"  Failed for image {i}: {e}")
        except Exception as e:
            print(f"Failed to fetch for {query}: {e}")

if __name__ == "__main__":
    download_images()
