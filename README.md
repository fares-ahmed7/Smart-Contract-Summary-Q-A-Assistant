# 🚀 Smart Contract Summary & Q/A Assistant

## 📌 Overview

Smart Contract Summary & Q/A Assistant is a Retrieval-Augmented Generation (RAG) based web application that allows users to upload long documents such as contracts, insurance policies, and reports, then interact with them through an AI conversational assistant.

The system extracts document content, splits it into semantic chunks, generates embeddings, stores them in a vector database, and enables intelligent question answering with source citations and conversation memory.

---

## 🎯 Features

✅ Upload PDF and DOCX documents  
✅ Automatic document parsing and chunking  
✅ Semantic similarity search  
✅ AI-powered conversational question answering  
✅ Page-number source citations  
✅ Hybrid conversation memory (short-term + vector memory)  
✅ Guardrails for safe responses  
✅ Local microservice architecture  
✅ Interactive chat interface  

---

## 🏗 System Architecture

### 🖥 Frontend
- Gradio chat interface
- File ingestion pipeline
- User interaction controller

### ⚙ Backend
- FastAPI microservice
- LangServe routing
- LLM inference engine

### 🧠 AI Pipeline

1. Text extraction from uploaded documents  
2. Text chunking  
3. Embedding generation  
4. Vector storage using Chroma  
5. Semantic retrieval  
6. Answer generation using LLM  

---

## 🛠 Technology Stack

| Category | Tools |
|----------|------------|
| Backend | FastAPI |
| RAG Framework | LangChain + LangServe |
| Frontend | Gradio |
| Vector Database | Chroma |
| Embeddings | Sentence Transformers |
| LLM | HuggingFace Models |
| Document Loaders | PyMuPDF, python-docx |
| Parsing | Unstructured |
| Environment Management | Python-dotenv |

---

## 📂 Project Structure
─ chroma_db_storage/     # Vector database storage ├── Backend.ipynb          # Backend server logic ├── Frontend.ipynb         # Gradio interface + document pipeline ├── .env                   # API keys configuration ├── requirements.txt       # Dependencies └── README.md              # Documentation

---

## ⚙️ Installation

### 1️⃣ Clone Repository

git clone <YOUR_REPOSITORY_LINK>
cd Smart-Contract-Summary-Q-A-Assistant

### 2️⃣ Create Virtual Environment

python -m venv .venv
source .venv/bin/activate      # Linux / Mac
.venv\Scripts\activate         # Windows

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Configure Environment Variables
Create .env file:
HF_TOKEN=your_huggingface_token

### ▶️ Running The Project
Start Backend Server
uvicorn server:app --port 9017

Start Frontend Interface
Run:
Frontend.ipynb
