import re

def search_html():
    html_path = r"C:\Users\DELL\Desktop\goat disease image - Search_files\saved_resource.html"
    try:
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        print(f"Content size: {len(content)} characters")
        
        # Let's find "Jaw Swelling" and extract around it
        idx = content.find("Jaw Swelling")
        if idx != -1:
            print(f"FOUND 'Jaw Swelling' at index {idx} in HTML.")
            # Print 2000 chars around it
            start = max(0, idx - 100)
            end = min(len(content), idx + 20000)
            print("Extracted snippet from HTML:")
            print(content[start:end])
            
            # Let's write to a text file for inspection
            with open(r"C:\Users\DELL\.gemini\antigravity\scratch\html_snippet.txt", "w", encoding="utf-8") as out:
                out.write(content[start:end])
            print("Snippet saved to html_snippet.txt")
        else:
            print("Did not find 'Jaw Swelling' in HTML.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_html()
