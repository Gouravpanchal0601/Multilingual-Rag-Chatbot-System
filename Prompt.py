# query.py
from langdetect import detect
import numpy as np

def query_index(query, embedding_index, top_k=3):
    """
    Search FAISS index for the top_k relevant chunks.
    """
    q_lang = detect(query)
    q_emb = embedding_index.encode([query])
    D, I = embedding_index.index.search(q_emb, top_k)

    results = []
    for idx in I[0]:
        results.append(embedding_index.tagged_chunks[idx])
    return q_lang, results
