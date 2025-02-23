import ocrmypdf

# Define input and output file names
input_pdf = "book.pdf"
output_pdf = "book_final.pdf"

# Apply OCR with improved settings
ocrmypdf.ocr(input_pdf, output_pdf,
    language="eng",
    force_ocr=True,             # Ensure OCR is applied to all pages
    optimize=1                  # Optimize PDF size
)

print(f"OCR complete. Searchable PDF saved as '{output_pdf}'")