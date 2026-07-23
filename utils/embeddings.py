from sentence_transformers import SentenceTransformer

# Load the embedding model only once
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def create_embeddings(chunks):
    """
    Converts text chunks into embedding vectors.

    Args:
        chunks (list): List of text chunks.

    Returns:
        list: Embedding vectors.
    """

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings