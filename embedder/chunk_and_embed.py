from sentence_transformers import SentenceTransformer
import textwrap

# Load model once globally
model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_texts(pages, max_chars=500):
    """
    Splits each page's text into chunks of ~max_chars.
    Input: dict {title: text}
    Output: list of strings [chunk1, chunk2, ...]
    """
    chunks = []
    for title, text in pages.items():
        parts = textwrap.wrap(text, width=max_chars, break_long_words=False)
        for part in parts:
            chunks.append(f"[{title}]\n{part.strip()}")
    return chunks

def embed_chunks(chunks):
    """
    Converts a list of text chunks into 384-dim embeddings.
    """
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings