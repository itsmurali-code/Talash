import streamlit as st
from scraper.wiki_scraper import scrape_wikipedia_pages
from embedder.chunk_and_embed import chunk_texts, embed_chunks
from indexer.faiss_index import create_faiss_index, search_faiss_index
from qa_model.answer_question import get_answer

st.set_page_config(page_title="Talash – Wikipedia Q&A", layout="centered")
st.title("🔍 Talash – Wikipedia Answer Finder")

# User inputs
urls_input = st.text_area("Enter Wikipedia URLs (comma-separated)")
question = st.text_input("Ask a question that requires context from all the URLs:")

if st.button("Search Answer"):
    with st.spinner("Scraping Wikipedia pages..."):
        pages = scrape_wikipedia_pages(urls_input)

    with st.spinner("Chunking & Embedding..."):
        chunks = chunk_texts(pages)
        embeddings = embed_chunks(chunks)

    with st.spinner("Searching relevant chunks..."):
        index = create_faiss_index(embeddings)
        top_chunks = search_faiss_index(index, embeddings, question, chunks)

    with st.spinner("Generating Answer..."):
        answer = get_answer(question, top_chunks)
        st.success(answer)