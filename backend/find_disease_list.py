import os
import zipfile
import sys

def search_in_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ['.pdf', '.docx', '.xlsx', '.txt', '.csv', '.json', '.html', '.xml']:
        return False
        
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Search UTF-8/ASCII
        if b"Jaw Swelling" in content or b"jaw swelling" in content or b"chewing" in content:
            print(f"FOUND in binary search of: {file_path}", flush=True)
            return True
            
        # Search UTF-16 LE
        if "Jaw Swelling".encode('utf-16-le') in content or "chewing".encode('utf-16-le') in content:
            print(f"FOUND in UTF-16-LE search of: {file_path}", flush=True)
            return True
            
        # If it's a zip file (like docx, xlsx)
        if ext in ['.docx', '.xlsx'] and zipfile.is_zipfile(file_path):
            try:
                with zipfile.ZipFile(file_path) as z:
                    for name in z.namelist():
                        if name.endswith('.xml') or name.endswith('.txt') or name.endswith('.csv'):
                            xml_content = z.read(name)
                            if b"Jaw Swelling" in xml_content or b"chewing" in xml_content:
                                print(f"FOUND inside zip/office file {file_path} -> {name}", flush=True)
                                return True
            except:
                pass
    except Exception as e:
        pass
    return False

def search_folders():
    paths = [
        r"C:\Users\DELL\Downloads",
        r"C:\Users\DELL\Desktop",
        r"C:\Users\DELL\Documents",
        r"C:\Users\DELL\.gemini\antigravity"
    ]
    
    print("Searching folders for 'Jaw Swelling' or 'chewing'...", flush=True)
    for folder in paths:
        if not os.path.exists(folder):
            continue
        print(f"Scanning folder: {folder}", flush=True)
        for root, dirs, files in os.walk(folder):
            if "node_modules" in root or "venv" in root or ".git" in root:
                continue
            for file in files:
                full_path = os.path.join(root, file)
                search_in_file(full_path)
    print("Search completed.", flush=True)

if __name__ == "__main__":
    search_folders()
