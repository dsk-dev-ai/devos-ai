from embeddings.model import embed
from .retriever import search

def run_rag(query):

    query_vector = embed([query])[0]

    docs = search(query_vector)

    context = "\n".join(docs)

    prompt = f"""
Use the following code context to answer.

{context}

Question: {query}
"""

    return prompt