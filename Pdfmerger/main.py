
from PyPDF2 import PdfMerger

# Create a PdfMerger object

merger = PdfMerger()

pdf_files = []
n =int(input(f"How many pdfs do you want to merge?\n"))

for i in range(0, n):
    name = input(f"Enter the name of the of pdf {i + 1}:")
    pdf_files.append(name)
    
# Add each PDF file to the merger
for pdf in pdf_files:
    merger.append(pdf)

# Save the merged PDF to a new file
merger.write("merged_output.pdf")
merger.close()

print("PDFs merged successfully!")


