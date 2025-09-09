# embeddings.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class EmbeddingIndex:
    def __init__(self, model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.tagged_chunks = []

    def build_index(self, tagged_chunks):
        """Generate embeddings and build FAISS index."""
        self.tagged_chunks = tagged_chunks
        embeddings = self.model.encode([c['text'] for c in tagged_chunks])
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        return self.index

    def encode(self, texts):
        return self.model.encode(texts)
