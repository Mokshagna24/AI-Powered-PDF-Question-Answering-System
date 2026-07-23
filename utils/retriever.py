import numpy as np

from utils.embeddings import embedding_model


def retrieve_chunks(index, chunks, query, top_k=5):
    """
    Retrieves the most relevant chunks for a user's query.

    Args:
        index : FAISS index
        chunks : Original text chunks
        query : User question
        top_k : Number of chunks to retrieve

    Returns:
        list : Most relevant chunks
    """

    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        np.array(
            query_embedding,
            dtype="float32"
        ),
        top_k
    )

    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(
            chunks[idx]
        )

    return retrieved_chunks