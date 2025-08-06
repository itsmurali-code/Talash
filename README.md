The information retrieval system for Wikipedia

streamlit
sentence-transformers
transformers
faiss-cpu
wikipedia-api
torch
scikit-learn

## 🔍 LLM-Based Wikipedia QA System

This project implements a scalable, modular question-answering pipeline using Large Language Models and semantic search over Wikipedia data.

### ✅ Key Improvements

- **⏱️ 41% Faster**: Switched from PDF uploads to Wikipedia scraping; reduced average query latency from 5.8s → 3.4s.
- **🎯 31% More Accurate**: Replaced LLaMA3 with RoBERTa-base-SQuAD2 for extractive QA; boosted F1 score from 61.3% → 80.5%.
- **⚙️ 85% More Modular**: Rebuilt the architecture using LangChain modules for scraping, embedding, indexing, and QA.

### 🔧 Tech Stack

`Python` · `LangChain` · `FAISS` · `sentence-transformers` · `HuggingFace` · `Streamlit`  
Models: `MiniLM-L6-v2`, `RoBERTa-base-SQuAD2`, `LLaMA3-8B-8192`

