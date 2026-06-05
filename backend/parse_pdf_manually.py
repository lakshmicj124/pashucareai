import zlib
import re
import os

def parse_pdf():
    pdf_path = r"C:\Users\DELL\Downloads\Livestock_Diseases_Dataset.pdf"
    if not os.path.exists(pdf_path):
        print("PDF file not found.")
        return
        
    try:
        with open(pdf_path, 'rb') as f:
            data = f.read()
        
        print(f"PDF Size: {len(data)} bytes")
        
        # Search raw bytes first
        if b"Jaw Swelling" in data or b"jaw swelling" in data or b"chewing" in data:
            print("Found in raw PDF bytes!")
            
        # Find all stream objects in PDF
        # PDF streams are enclosed between 'stream' and 'endstream'
        stream_count = 0
        decompressed_count = 0
        all_text = ""
        
        # Simple regex to find streams. They usually have a dict before them specifying /Filter /FlateDecode
        # We can find all occurrences of b'stream' and b'endstream'
        start_indices = [m.start() for m in re.finditer(b'stream\r?\n', data)]
        end_indices = [m.start() for m in re.finditer(b'endstream', data)]
        
        print(f"Found {len(start_indices)} stream starts and {len(end_indices)} stream ends.")
        
        for start_idx in start_indices:
            # Find the closest end_idx after start_idx
            valid_ends = [e for e in end_indices if e > start_idx]
            if not valid_ends:
                continue
            end_idx = valid_ends[0]
            
            # Extract stream content (skip the 'stream\r\n' or 'stream\n' itself)
            stream_data = data[start_idx : end_idx]
            # Strip starting 'stream' and leading/trailing newlines
            if stream_data.startswith(b'stream\r\n'):
                stream_content = stream_data[8:]
            elif stream_data.startswith(b'stream\n'):
                stream_content = stream_data[7:]
            else:
                stream_content = stream_data[6:]
                
            # Decompress stream
            try:
                dec = zlib.decompress(stream_content)
                decompressed_count += 1
                dec_text = dec.decode('utf-8', errors='ignore')
                all_text += dec_text + "\n"
            except Exception as e:
                # Try raw inflate
                try:
                    dec = zlib.decompress(stream_content, -zlib.MAX_WBITS)
                    decompressed_count += 1
                    dec_text = dec.decode('utf-8', errors='ignore')
                    all_text += dec_text + "\n"
                except:
                    pass
                    
        print(f"Successfully decompressed {decompressed_count} streams.")
        
        # Search decompressed text
        if "Jaw Swelling" in all_text or "jaw swelling" in all_text or "chewing" in all_text:
            print("FOUND match in decompressed PDF text!")
            # Find all matches of symptoms or disease names
            # Let's save the entire decompressed text to check it
            with open(r"C:\Users\DELL\.gemini\antigravity\scratch\pdf_text.txt", "w", encoding="utf-8") as out:
                out.write(all_text)
            print("Saved decompressed text to pdf_text.txt")
        else:
            print("Did not find target words in decompressed PDF text.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parse_pdf()
