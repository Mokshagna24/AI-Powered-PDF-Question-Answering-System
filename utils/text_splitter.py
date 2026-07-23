from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text):
    """
    Splits extracted text into overlapping chunks.

    Args:
        text (str): Complete text extracted from PDFs.

    Returns:
        list: List of text chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_text(text)

    return chunks