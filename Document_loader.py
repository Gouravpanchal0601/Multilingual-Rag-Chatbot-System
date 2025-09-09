# ingestion.py
import pdfplumber

def load_pdf(pdf_path):
    """Load PDF and extract text from all pages."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text