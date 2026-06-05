import os

def search_logs():
    brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain"
    if not os.path.exists(brain_dir):
        print("Brain directory not found.")
        return
        
    print("Searching conversation logs...")
    matches = []
    for root, dirs, files in os.walk(brain_dir):
        for file in files:
            if file == "overview.txt":
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    if "Jaw Swelling" in content:
                        matches.append(full_path)
                        print(f"FOUND match in: {full_path}")
                except Exception as e:
                    pass
                    
    print(f"Found {len(matches)} matching logs.")

if __name__ == "__main__":
    search_logs()
