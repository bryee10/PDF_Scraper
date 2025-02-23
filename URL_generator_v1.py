page_numbers = [1, 2, 3, 4, 5]  # Replace with the full list of pages
base_url = "page_URL_with_page_number"
output_file = "horizontal_pages.txt"

# Write the hyperlinked text to the file with updated formatting
with open(output_file, "w") as file:
    for page_num in page_numbers:
        file.write(f"Page {page_num}:\n{base_url.format(page_num)}\n-----------------------------------------\n\n")

print(f"✅ File '{output_file}' created successfully.")
