from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
num_files = int(input("Enter the number of PDF files to Merge: "))

for i in range(num_files):
    file_name = input(f"Enter the path for file {i+1}: ")
    reader = PdfReader(file_name)
    
    if reader.is_encrypted:
        print(f"Skipping encrypted file: {file_name}")
        continue  # Skip encrypted PDFs
    
    for page in reader.pages:
        writer.add_page(page)

output_file = input("Enter the name for the merged file ")
if not output_file.endswith(".pdf"):
    output_file += ".pdf"

if len(writer.pages) == 0:
    print("No pages were added. Check your input files.")
else:
    with open(output_file, 'wb') as output:
        writer.write(output)
    print(f"Merged PDF saved as {output_file}")
