import fitz  # PyMuPDF (to extract text from PDF)
from O365 import Account
import os

# Set up OneDrive authentication
credentials = (os.getenv("ONEDRIVE_CLIENT_ID"), os.getenv("ONEDRIVE_CLIENT_SECRET"))
account = Account(credentials)

if account.authenticate(scopes=['basic', 'onedrive_all']):
    storage = account.storage()
    drive = storage.get_default_drive()

    # Change this path to match the PDF location in OneDrive
    file_path = "Documents/PDFs/sample.pdf"
    file = drive.get_item_by_path(file_path)
    file_content = file.get_content()

    # Save PDF locally
    with open("sample.pdf", "wb") as pdf_file:
        pdf_file.write(file_content)

    # Extract text from PDF
    pdf_document = fitz.open("sample.pdf")
    extracted_text = "\n".join([page.get_text() for page in pdf_document])

    print("Extracted Text:\n", extracted_text)

    with open("extracted_text.txt", "w", encoding="utf-8") as text_file:
        text_file.write(extracted_text)
