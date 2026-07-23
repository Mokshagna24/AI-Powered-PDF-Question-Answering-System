import os
import pickle

import faiss
import numpy as np


VECTOR_DB_PATH = "vector_db"


def create_vector_store(chunks, embeddings):
    """
    Creates and saves a FAISS vector database.

    Args:
        chunks (list): List of text chunks.
        embeddings (numpy.ndarray): Embedding vectors.
    """

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(
        np.array(
            embeddings,
            dtype="float32"
        )
    )

    faiss.write_index(index,
        os.path.join(VECTOR_DB_PATH,"index.faiss")
    )

    with open(
        os.path.join(VECTOR_DB_PATH,"chunks.pkl"),
        "wb") as f:

        pickle.dump(chunks,f)


def load_vector_store():
    """
    Loads FAISS index and chunks.

    Returns:
        tuple:
            index,
            chunks
    """

    index = faiss.read_index(
        os.path.join(
            VECTOR_DB_PATH,
            "index.faiss"
        )
    )

    with open(
        os.path.join(
            VECTOR_DB_PATH,
            "chunks.pkl"
        ),
        "rb"
    ) as f:

        chunks = pickle.load(f)

    return index, chunks