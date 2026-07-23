from pypdf import PdfReader


def load_pdf(uploaded_file):
    """
    Extracts text from a single uploaded PDF.

    Args:
        uploaded_file: Streamlit UploadedFile object

    Returns:
        str: Complete extracted text from the PDF
    """

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"  """append because of none value may occur in case of non-text materials/characters"""

    return text