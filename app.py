import streamlit as st

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.embeddings import create_embeddings
from utils.vector_store import (
    create_vector_store,
    load_vector_store
)
from utils.retriever import retrieve_chunks
from utils.prompt import build_prompt
from utils.llm import generate_answer


st.set_page_config(
    page_title="PDF AI Assistant",
    page_icon="📄",
    layout="wide"
)


st.title("📄 PDF AI Assistant")

st.write(
    "Upload a PDF and ask questions about it."
)


uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


if uploaded_file:

    with st.spinner("Reading PDF..."):

        text = load_pdf(uploaded_file)

        chunks = split_text(text)

        embeddings = create_embeddings(chunks)

        create_vector_store(
            chunks,
            embeddings
        )

    st.success("PDF processed successfully!")

    index, chunks = load_vector_store()

    question = st.text_input(
        "Ask a Question"
    )

    if question:

        retrieved_chunks = retrieve_chunks(
            index,
            chunks,
            question
        )

        prompt = build_prompt(
            retrieved_chunks,
            question
        )

        with st.spinner("Generating Answer..."):

            answer = generate_answer(
                prompt
            )

        st.subheader("Answer")

        st.write(answer)