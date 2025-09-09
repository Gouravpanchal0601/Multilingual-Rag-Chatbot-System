# tagging.py
from langdetect import detect

def tag_chunks(chunks, source):
    """
    Tag each chunk with language and source.
    """
    tagged_chunks = []
    for c in chunks:
        if c.strip():
            lang = detect(c)
            tagged_chunks.append({
                "text": c,
                "lang": lang,
                "source": source
            })
    return tagged_chunks
