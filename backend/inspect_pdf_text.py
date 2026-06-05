import zlib
import re
import os

def extract_all():
    pdf_path = r"C:\Users\DELL\Downloads\Livestock_Diseases_Dataset.pdf"
    if not os.path.exists(pdf_path):
        print("PDF not found.")
        return
        
    with open(pdf_path, 'rb') as f:
        data = f.read()
        
    start_indices = [m.start() for m in re.finditer(b'stream\r?\n', data)]
    end_indices = [m.start() for m in re.finditer(b'endstream', data)]
    
    all_text = ""
    for start_idx in start_indices:
        valid_ends = [e for e in end_indices if e > start_idx]
        if not valid_ends:
            continue
        end_idx = valid_ends[0]
        
        stream_data = data[start_idx : end_idx]
        if stream_data.startswith(b'stream\r\n'):
            stream_content = stream_data[8:]
        elif stream_data.startswith(b'stream\n'):
            stream_content = stream_data[7:]
        else:
            stream_content = stream_data[6:]
            
        try:
            dec = zlib.decompress(stream_content)
            dec_text = dec.decode('utf-8', errors='ignore')
            all_text += dec_text + "\n"
        except:
            try:
                dec = zlib.decompress(stream_content, -zlib.MAX_WBITS)
                dec_text = dec.decode('utf-8', errors='ignore')
                all_text += dec_text + "\n"
            except:
                pass
                
    # Now find all text inside parentheses
    matches = re.findall(r'\((.*?)\)', all_text)
    print(f"Total parenthesized strings: {len(matches)}")
    print("First 50 strings:")
    for m in matches[:50]:
        if len(m.strip()) > 1 and len(m) < 100:
            print(f"  - {m}")
            
    # Search for any matches of standard words like "Abdomen" or "Fever"
    print("\nSearch for 'Fever':")
    for m in matches:
        if "fever" in m.lower():
            print(f"  - {m}")

if __name__ == "__main__":
    extract_all()
