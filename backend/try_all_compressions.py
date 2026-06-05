import bz2
import lzma
import zipfile
import os

def try_all():
    pb_path = r"C:\Users\DELL\.gemini\antigravity\conversations\2b26c8ee-eb61-4897-a3af-76a6464c8556.pb"
    if not os.path.exists(pb_path):
        print("PB file not found.")
        return
        
    with open(pb_path, 'rb') as f:
        data = f.read()
        
    print(f"Data size: {len(data)}")
    
    # Try bz2
    try:
        dec = bz2.decompress(data)
        print("Decompressed with bz2 successfully!")
        check_text(dec)
        return
    except Exception as e:
        print(f"bz2 failed: {e}")
        
    # Try lzma
    try:
        dec = lzma.decompress(data)
        print("Decompressed with lzma successfully!")
        check_text(dec)
        return
    except Exception as e:
        print(f"lzma failed: {e}")
        
    # Try zipfile
    if zipfile.is_zipfile(pb_path):
        print("It is a zip file! Extracting...")
        try:
            with zipfile.ZipFile(pb_path) as z:
                for name in z.namelist():
                    print(f"Zip member: {name}")
                    member_data = z.read(name)
                    check_text(member_data)
        except Exception as e:
            print(f"Zip extraction failed: {e}")

def check_text(dec_data):
    text = dec_data.decode('utf-8', errors='ignore')
    print(f"Decompressed length: {len(text)}")
    if "Jaw Swelling" in text:
        print("FOUND 'Jaw Swelling' in decompressed text!")
        idx = text.find("Jaw Swelling")
        with open(r"C:\Users\DELL\.gemini\antigravity\scratch\uncompressed_pb.txt", "w", encoding="utf-8") as f:
            f.write(text[idx - 200 : idx + 20000])
        print("Extracted snippet saved to uncompressed_pb.txt")
    else:
        print("Did not find 'Jaw Swelling'.")

if __name__ == "__main__":
    try_all()
