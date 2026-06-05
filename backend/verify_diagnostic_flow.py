import urllib.request
import urllib.parse
import json
import os
import mimetypes

BASE_URL = "http://127.0.0.1:8000"
HEALTHY_IMG = r"c:\Users\DELL\Documents\cow disease project\dataset\goat\healthy\healthy goat_1.jpeg"
DISEASED_IMG = r"c:\Users\DELL\Documents\cow disease project\dataset\goat\mange\mock_0.jpg"

def post_json(url, data_dict, headers=None):
    if headers is None:
        headers = {}
    headers["Content-Type"] = "application/json"
    req_data = json.dumps(data_dict).encode("utf-8")
    req = urllib.request.Request(url, data=req_data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8")
    except Exception as e:
        return 500, str(e)

def upload_file(url, file_path, form_fields, headers=None):
    if headers is None:
        headers = {}
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    parts = []
    
    # Add files
    file_name = os.path.basename(file_path)
    mime_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
    
    with open(file_path, "rb") as f:
        file_content = f.read()
        
    parts.append(f"--{boundary}")
    parts.append(f'Content-Disposition: form-data; name="file"; filename="{file_name}"')
    parts.append(f"Content-Type: {mime_type}")
    parts.append("")
    parts.append(file_content)
    
    # Add form fields
    for key, value in form_fields.items():
        parts.append(f"--{boundary}")
        parts.append(f'Content-Disposition: form-data; name="{key}"')
        parts.append("")
        parts.append(str(value).encode("utf-8"))
        
    parts.append(f"--{boundary}--")
    parts.append(b"")
    
    # Construct body
    body = b""
    for part in parts:
        if isinstance(part, str):
            body += (part + "\r\n").encode("utf-8")
        else:
            body += part + b"\r\n"
            
    headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
    
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8")
    except Exception as e:
        return 500, str(e)

def run_tests():
    print("====================================================")
    print("      VERIFYING FASTAPI ENDPOINTS & DIAGNOSTICS     ")
    print("====================================================\n")
    
    email = "testflowuser123@example.com"
    password = "SecurePassword123!"
    
    # 1. Attempt login
    print(f"[1] Attempting login: {email}")
    status, res = post_json(f"{BASE_URL}/api/auth/login", {"email": email, "password": password})
    auth_token = None
    
    if status == 200:
        print("[SUCCESS] Logged in successfully!")
        auth_token = res["token"]
    else:
        print(f"[1] User not found or login failed (status={status}). Registering new user...")
        # Register new user
        reg_data = {
            "name": "Flow Test User",
            "email": email,
            "phone_number": "9876543201",
            "password": password
        }
        status, res = post_json(f"{BASE_URL}/api/auth/register", reg_data)
        if status == 200:
            print("[SUCCESS] Registered new user successfully!")
            auth_token = res["token"]
        else:
            print(f"[FAIL] Registration failed (status={status}): {res}")
            return

    headers = {"Authorization": f"Bearer {auth_token}"}
    
    # 2. Upload healthy goat image
    print("\n[2] Uploading HEALTHY goat image...")
    if not os.path.exists(HEALTHY_IMG):
        print(f"[FAIL] Healthy image not found at: {HEALTHY_IMG}")
        return
        
    status, result = upload_file(
        f"{BASE_URL}/api/detect",
        HEALTHY_IMG,
        {"animal_type": "Goat", "lang": "en"},
        headers
    )
    
    if status == 200:
        print(f"[SUCCESS] Healthy image processed!")
        print(f"  Predicted Disease: {result.get('disease_name')}")
        print(f"  Confidence: {result.get('confidence')}%")
        print(f"  Symptoms Listed: {result.get('symptoms')}")
        print(f"  Causes/Reasons: {result.get('why_it_happened') or result.get('causes')}")
    else:
        print(f"[FAIL] Healthy image upload failed (status={status}): {result}")
        
    # 3. Upload diseased goat image
    print("\n[3] Uploading DISEASED goat image...")
    if not os.path.exists(DISEASED_IMG):
        print(f"[FAIL] Diseased image not found at: {DISEASED_IMG}")
        return
        
    status, result = upload_file(
        f"{BASE_URL}/api/detect",
        DISEASED_IMG,
        {"animal_type": "Goat", "lang": "en"},
        headers
    )
    
    if status == 200:
        print(f"[SUCCESS] Diseased image processed!")
        print(f"  Predicted Disease: {result.get('disease_name')}")
        print(f"  Confidence: {result.get('confidence')}%")
        print(f"  Symptoms: {result.get('symptoms')}")
        print(f"  Causes: {result.get('why_it_happened') or result.get('causes')}")
        print(f"  Prevention: {result.get('prevention')}")
        print(f"  Recommended Feed: {result.get('food_recommendations')}")
        print(f"  Veterinary Guidance: {result.get('hygiene_tips') or result.get('first_aid')}")
    else:
        print(f"[FAIL] Diseased image upload failed (status={status}): {result}")

if __name__ == "__main__":
    run_tests()
