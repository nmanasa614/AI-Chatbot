from pypdf import PdfReader
from PIL import Image

def extract_pdf_text(uploaded_file):

    pdf_reader = PdfReader(
        uploaded_file
    )

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text

    return text

def load_image(uploaded_image):

    return Image.open(
        uploaded_image
    )