import zipfile
import os

def list_archive(zip_path):
    if not os.path.exists(zip_path):
        print(f"File not found: {zip_path}")
        return
        
    print(f"\n--- Listing {os.path.basename(zip_path)} ---")
    try:
        with zipfile.ZipFile(zip_path) as z:
            names = z.namelist()
            print(f"Total files: {len(names)}")
            
            # Print files matching keyword or first 20 files
            matching = [n for n in names if any(x in n.lower() for x in ["goat", "disease", "symptom", "dataset", "txt", "csv", "json"])]
            print(f"Matching files ({len(matching)}):")
            for m in matching[:50]:
                print(f"  - {m}")
            if len(matching) > 50:
                print("  ... and more")
                
            # If no matches, print first 10 files
            if not matching:
                print("No keyword matches. First 10 files:")
                for n in names[:10]:
                    print(f"  - {n}")
                    
            # Let's search inside the text files in the zip for 'Jaw Swelling' or 'chewing'
            for name in names:
                if name.endswith(('.txt', '.csv', '.json', '.xml', '.html')):
                    try:
                        content = z.read(name)
                        if b"Jaw Swelling" in content or b"chewing" in content:
                            print(f"\nFOUND MATCH inside: {zip_path} -> {name}")
                            # Print a snippet
                            print(content[:1000].decode('utf-8', errors='ignore'))
                    except Exception as e:
                        pass
                        
    except Exception as e:
        print(f"Error reading zip: {e}")

if __name__ == "__main__":
    list_archive(r"C:\Users\DELL\Downloads\archive.zip")
    # archive (1).zip is 268MB, let's just search its file names first
    list_archive(r"C:\Users\DELL\Downloads\archive (1).zip")
