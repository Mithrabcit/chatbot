
from pypdf import PdfReader

# Location of your electricity tariff PDF
pdf_path = r"C:\Users\DELL\Downloads\llm-fastapi-project\data\electricity\_copy.pdf"

# Open the PDF
reader = PdfReader(pdf_path)

# Extract text from every page
all_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        all_text += text + "\n"

# Display the extracted text
print(all_text[:5000])

# Save extracted text into a file
with open("electricity_data.txt", "w", encoding="utf-8") as file:
    file.write(all_text)

print("\nPDF text extracted successfully!")

