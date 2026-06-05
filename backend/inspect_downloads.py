import csv
import os

def inspect_csv():
    csv_path = r"C:\Users\DELL\Downloads\Testing.csv"
    if os.path.exists(csv_path):
        print("Testing.csv exists. Reading first 5 rows:")
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if i < 5:
                        print(row)
                    else:
                        break
        except Exception as e:
            print(f"Error reading CSV: {e}")
    else:
        print("Testing.csv does not exist.")

def inspect_pdf():
    pdf_path = r"C:\Users\DELL\Downloads\Livestock_Diseases_Dataset.pdf"
    if os.path.exists(pdf_path):
        print("Livestock_Diseases_Dataset.pdf exists. Checking if we can read text using a basic script or pdf reader:")
        try:
            # We can check if PyPDF2 or pdfplumber or pypdf is installed, or try importing standard libraries
            import importlib.util
            for lib in ['pypdf', 'PyPDF2', 'pdfplumber', 'fitz']:
                spec = importlib.util.find_spec(lib)
                if spec is not None:
                    print(f"Library {lib} is installed!")
                    # Try reading text
                    if lib == 'pypdf' or lib == 'PyPDF2':
                        from pypdf import PdfReader
                        reader = PdfReader(pdf_path)
                        text = ""
                        for page in reader.pages[:3]:
                            text += page.extract_text() or ""
                        print("Sample PDF text:")
                        print(text[:1000])
                        return
            print("No PDF libraries found in the active environment.")
        except Exception as e:
            print(f"Error reading PDF: {e}")
    else:
        print("PDF does not exist.")

if __name__ == "__main__":
    inspect_csv()
    inspect_pdf()
