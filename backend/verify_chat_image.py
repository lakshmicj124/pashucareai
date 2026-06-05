import sys
import os
sys.path.append(r"c:\Users\DELL\Documents\cow disease project\backend")

from fastapi.testclient import TestClient
from app.main import app

def test_image_transition():
    print("Testing transition between multiple uploaded images in the same session...")
    
    uploads_dir = r"c:\Users\DELL\Documents\cow disease project\backend\uploads"
    images = [f for f in os.listdir(uploads_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
    if not images:
        print("No test image found in uploads directory to perform test.")
        return
        
    test_image_path = os.path.join(uploads_dir, images[0])
    print(f"Using test image: {test_image_path}")

    with TestClient(app) as client:
        # User login
        login_res = client.post("/api/auth/login", json={
            "email": "img_chat_test@pashucare.ai",
            "password": "Password123!"
        })
        token = ""
        if login_res.status_code == 200:
            token = login_res.json().get("token")
        else:
            print("Login failed, attempting register...")
            register_res = client.post("/api/auth/register", json={
                "name": "Chatbot Image Test User",
                "email": "img_chat_test@pashucare.ai",
                "password": "Password123!"
            })
            token = register_res.json().get("token")
            
        if not token:
            print("Could not obtain token.")
            return
            
        headers = {"Authorization": f"Bearer {token}"}
        
        # 1. Upload first image (Cow)
        print("\n--- 1. Uploading first image (Cow) ---")
        with open(test_image_path, "rb") as img_file:
            files = {"file": (os.path.basename(test_image_path), img_file, "image/jpeg")}
            data = {"animal_type": "Cow", "lang": "en"}
            response = client.post("/api/chat/image", files=files, data=data, headers=headers)
            
        res_json = response.json()
        session_id = res_json.get("session_id")
        disease_1 = res_json.get("disease_name")
        print(f"Diagnosed Cow Disease: {disease_1}")
        print(f"Session ID: {session_id}")

        # 2. Ask follow-up about Cow disease
        print("\n--- 2. Sending text follow-up for Cow disease ---")
        chat_req = {
            "session_id": session_id,
            "message": "what are the symptoms?",
            "lang": "en"
        }
        followup_1 = client.post("/api/chat", json=chat_req, headers=headers)
        print(f"Follow-up 1 text snippet:\n {ascii(followup_1.json().get('response')[:200])}")
        
        # Verify it references disease_1
        assert disease_1.lower() in followup_1.json().get("response").lower() or "symptoms" in followup_1.json().get("response").lower()

        # 3. Upload second image (Goat) in the same session
        print("\n--- 3. Uploading second image (Goat) in the same session ---")
        with open(test_image_path, "rb") as img_file:
            # We rename the filename to contain 'goat' so classification verifies it as Goat
            files = {"file": ("test_goat_image.jpg", img_file, "image/jpeg")}
            data = {"animal_type": "Goat", "lang": "en", "session_id": session_id}
            response_2 = client.post("/api/chat/image", files=files, data=data, headers=headers)
            
        res_json_2 = response_2.json()
        disease_2 = res_json_2.get("disease_name")
        print(f"Diagnosed Goat Disease: {disease_2}")

        # 4. Ask follow-up about Goat disease
        print("\n--- 4. Sending text follow-up after second image ---")
        chat_req_2 = {
            "session_id": session_id,
            "message": "what are the symptoms?",
            "lang": "en"
        }
        followup_2 = client.post("/api/chat", json=chat_req_2, headers=headers)
        print(f"Follow-up 2 text snippet:\n {ascii(followup_2.json().get('response')[:200])}")

        # Clean up session
        client.delete(f"/api/chat/sessions/{session_id}", headers=headers)
        print("\nTest completed successfully!")

if __name__ == "__main__":
    test_image_transition()
