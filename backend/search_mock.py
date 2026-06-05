import json

def search_mock():
    db_path = r"C:\Users\DELL\Documents\cow disease project\backend\mock_database.json"
    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        print("Loaded mock database. Type:", type(data))
        # Search recursively
        found = []
        def search_rec(obj, path=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    search_rec(v, f"{path}.{k}" if path else k)
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    search_rec(v, f"{path}[{i}]")
            elif isinstance(obj, str):
                if "Jaw" in obj or "jaw" in obj or "chewing" in obj:
                    found.append((path, obj))
                    
        search_rec(data)
        print(f"Found {len(found)} matches in mock_database.json:")
        for path, val in found:
            print(f"- Path: {path} -> {val[:200]}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_mock()
