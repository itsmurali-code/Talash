import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load the same model as used in embedder
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_faiss_index(embeddings):
    """
    Creates and returns a FAISS index given a list of embeddings.
    """
    dimension = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def search_faiss_index(index, embeddings, question, chunks, top_k=5):
    """
    Searches the FAISS index using the embedded question and returns top_k chunks.
    """
    question_embedding = model.encode([question])
    D, I = index.search(np.array(question_embedding), top_k)
    top_chunks = [chunks[i] for i in I[0]]
    return top_chunks