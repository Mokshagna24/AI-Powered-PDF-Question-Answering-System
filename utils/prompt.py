def build_prompt(context_chunks, question):
    """
    Builds the prompt sent to the LLM.

    Args:
        context_chunks (list): Retrieved text chunks.
        question (str): User question.

    Returns:
        str: Complete prompt.
    """

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the information provided in the context.

If the answer cannot be found in the context, say:
"I couldn't find that information in the uploaded document."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt