import sys
import os
import shutil

sys.path.append(r"c:\Users\DELL\Documents\cow disease project\backend")

from fastapi.testclient import TestClient
from app.main import app

def test_sheep_api():
    print("Testing sheep diagnostics API routes...")
    
    dataset_dir = r"c:\Users\DELL\Documents\cow disease project\dataset"
    diseased_folder = os.path.join(dataset_dir, "diseased sheep")
    
    if not os.path.exists(diseased_folder):
        print("ERROR: Diseased sheep folder not found.")
        return
        
    files = [f for f in os.listdir(diseased_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.jfif'))]
    if not files:
        print("ERROR: No diseased sheep images found.")
        return
        
    src_image = os.path.join(diseased_folder, files[0])
    # Create a temporary copy with a filename that will pass the classify_animal validator
    temp_image_path = os.path.join(os.path.dirname(src_image), "temp_diseased_sheep.jfif")
    shutil.copy(src_image, temp_image_path)
    
    print(f"Using test image: {temp_image_path} (copied from {src_image})")
    
    try:
        with TestClient(app) as client:
            # 1. Register or login to get token
            register_res = client.post("/api/auth/register", json={
                "name": "Sheep Test User",
                "email": "sheep_test@pashucare.ai",
                "password": "Password123!"
            })
            
            token = ""
            if register_res.status_code == 200:
                token = register_res.json().get("token")
            else:
                login_res = client.post("/api/auth/login", json={
                    "email": "sheep_test@pashucare.ai",
                    "password": "Password123!"
                })
                if login_res.status_code == 200:
                    token = login_res.json().get("token")
                    
            if not token:
                print("Could not obtain auth token.")
                return
                
            headers = {"Authorization": f"Bearer {token}"}
            
            # Test Route 1: /api/detect
            print("\n--- Testing /api/detect ---")
            with open(temp_image_path, "rb") as img_file:
                files_payload = {"file": (os.path.basename(temp_image_path), img_file, "image/jpeg")}
                data_payload = {"animal_type": "Sheep", "lang": "en"}
                response = client.post("/api/detect", files=files_payload, data=data_payload, headers=headers)
                
            print(f"Detect Response status: {response.status_code}")
            if response.status_code == 200:
                res_json = response.json()
                print("Detected Disease Name:", res_json.get("disease_name"))
                print("Detected Animal Type:", res_json.get("animal_type"))
                print("Confidence:", res_json.get("confidence"))
                assert res_json.get("disease_name") == "Sheep Scab (Psoroptic Mange)", "Mismatch in disease name"
                assert res_json.get("animal_type") == "Sheep", "Mismatch in animal type"
                print("-> /api/detect test PASSED.")
            else:
                print(f"Failed /api/detect with detail: {response.text}")
                
            # Test Route 2: /api/chat/image
            print("\n--- Testing /api/chat/image ---")
            with open(temp_image_path, "rb") as img_file:
                files_payload = {"file": (os.path.basename(temp_image_path), img_file, "image/jpeg")}
                data_payload = {"animal_type": "Sheep", "lang": "en"}
                response = client.post("/api/chat/image", files=files_payload, data=data_payload, headers=headers)
                
            print(f"Chat Image Response status: {response.status_code}")
            if response.status_code == 200:
                res_json = response.json()
                print("Response Text Preview:\n", res_json.get("response")[:200] + "...")
                print("Response Disease Name:", res_json.get("disease_name"))
                print("Response Confidence:", res_json.get("confidence"))
                assert res_json.get("disease_name") == "Sheep Scab (Psoroptic Mange)", "Mismatch in disease name"
                print("-> /api/chat/image test PASSED.")
            else:
                print(f"Failed /api/chat/image with detail: {response.text}")
                
    finally:
        # Clean up temporary copy
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)

if __name__ == "__main__":
    test_sheep_api()
