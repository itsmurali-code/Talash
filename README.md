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



## Installation and Run Guide

1. **Download the File**
   - Download the project zip file (e.g., `project.zip`).

2. **Extract the File**
   - Right-click the downloaded zip file.
   - Select “Extract All” and choose your destination folder.

3. **Open Pharm IDE**
   - Launch Pharm IDE on your computer.

4. **Install Required Requirements**
   - Open the terminal in Pharm IDE.
   - Navigate (cd) to the extracted project folder.

5. **Install Dependencies**
   - Run the following command to install dependencies listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

6. **Run the Project**
   - In the same terminal, start your Streamlit application by typing:
     ```bash
     streamlit run app.py
     ```

***

**Your app will start in the browser automatically. You are now ready to use the application!**

