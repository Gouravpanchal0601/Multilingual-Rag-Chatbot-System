# main.py
from ingestion import load_pdf
from chunking import chunk_text
from tagging import tag_chunks
from embeddings import EmbeddingIndex
from query import query_index

PDF_FILE = "Replace with your PDF FILE PATH"

# Step 1: Load PDF
text = load_pdf(PDF_FILE)

# Step 2: Chunk text
chunks = chunk_text(text)

# Step 3: Tag chunks with language and source
tagged_chunks = tag_chunks(chunks, PDF_FILE)

# Step 4: Build embeddings & FAISS index
embedding_index = EmbeddingIndex()
embedding_index.build_index(tagged_chunks)

# Step 5: Query the chatbot
if __name__ == "__main__":
    query = "what was the revenue in 2024"
    lang, results = query_index(query, embedding_index)

    print(f"Query Language: {lang}")
    print("Top 3 results:")
    for r in results:
        print(f"Text: {r['text']}\nSource: {r['source']}\n")
