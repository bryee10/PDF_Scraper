import os
import re
from PyPDF2 import PdfMerger

# Define the folder and output file
input_folder = "ind_pdfs"
output_pdf = "book.pdf"

# Function to extract page number from filename
def extract_page_number(filename):
    match = re.search(r"page_(\d+)\.pdf", filename)
    return int(match.group(1)) if match else float("inf")  # Default to a high number if no match

# Get all PDF files in the folder and sort them by page number
pdf_files = sorted(
    [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(".pdf")],
    key=lambda x: extract_page_number(os.path.basename(x))
)

# Merge PDFs
if pdf_files:
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()
    print(f"\n✅ Merged PDF saved as '{output_pdf}'")
else:
    print("❌ No PDFs found in 'ind_pdfs' folder.")
