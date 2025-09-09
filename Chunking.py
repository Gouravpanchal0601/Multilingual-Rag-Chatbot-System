# chunking.py

def chunk_text(text, max_len=500):
    """
    Split text into chunks for embeddings.
    """
    paragraphs = text.split("\n\n")
    chunks = []
    for p in paragraphs:
        words = p.strip().split()
        for i in range(0, len(words), max_len):
            chunks.append(" ".join(words[i:i+max_len]))
    return chunks
