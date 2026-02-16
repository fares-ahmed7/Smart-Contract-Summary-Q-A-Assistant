# 🚀 Smart-Contract-Summary-Q-A-Assistant

## 📌 Overview
This project is a small-scale Retrieval-Augmented Generation (RAG) web application that allows users to upload contracts, insurance policies, reports, or other long documents and interact with them using an AI conversational assistant.

The system extracts document content, chunks it, creates embeddings, stores them in a vector database, and enables chat-based question answering with guardrails and source citations.

---

## 🎯 Features

- Upload PDF and DOCX documents  
- Document chunking and embedding  
- Semantic similarity retrieval  
- AI-powered question answering  
- Page-number citations  
- Conversation memory support  
- Local microservice architecture  
- Interactive chat interface  

---

## 🏗 Architecture

### Frontend
- Gradio user interface  
- File ingestion pipeline  
- Retrieval controller  

### Backend
- FastAPI microservice  
- LangServe routing  
- LLM inference  

### AI Pipeline
- Text extraction  
- Chunking  
- Embeddings  
- Vector storage (Chroma)  
- Retrieval  
- Answer generation  

---

## 🛠 Technology Stack

- FastAPI  
- LangChain  
- LangServe  
- Gradio  
- Chroma Vector Database  
- Sentence Transformers Embeddings  
- PyMuPDF & python-docx loaders  
- HuggingFace LLM  
- Unstructured  
- Python-dotenv  

---

## 📂 Project Structure
├── chroma_db_storage/   # The vector database containing embedded document chunks
├── Backend.ipynb        # Server-side logic and LLM configuration
├── Frontend.ipynb       # Gradio UI and document processing pipeline
├── .env                 # Configuration file for API keys (e.g., HF_TOKEN)
├── requirements.txt     # List of required Python libraries
└── README.md            # Project documentation and setup guide






