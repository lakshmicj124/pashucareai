import re
import os

def find_pdf_text():
    pdf_text_path = r"C:\Users\DELL\.gemini\antigravity\scratch\pdf_text.txt"
    if not os.path.exists(pdf_text_path):
        print("pdf_text.txt does not exist.")
        return
        
    with open(pdf_text_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    print(f"File size: {len(content)}")
    
    # PDF text is usually inside ( ... ) Tj or [ ... ] TJ
    # Let's find matches of (something) Tj or (something)
    matches = re.findall(r'\((.*?)\)', content)
    print(f"Found {len(matches)} parenthesized items.")
    print("First 100 items:")
    for m in matches[:100]:
        # Filter out long drawings or strange strings
        if len(m.strip()) > 1 and len(m) < 100:
            print(f"  - {m}")
            
    # Search for "Jaw" or "Swelling" in the matched items
    print("\nSearching items for keywords:")
    for m in matches:
        if any(x in m.lower() for x in ["jaw", "swelling", "chewing", "kicking"]):
            print(f"  MATCH: {m}")

if __name__ == "__main__":
    find_pdf_text()
