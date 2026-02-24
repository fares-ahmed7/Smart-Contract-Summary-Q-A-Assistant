# 🚀 Smart Contract Summary & Q&A Assistant (RAG + Evaluation)

A local Retrieval-Augmented Generation (RAG) system with built-in evaluation for
question answering over long documents (PDF / DOCX), using strict anti-hallucination guardrails.

The project is fully script-based (no notebooks) and runs via:
- app.py (Gradio frontend)
- server_app.py (FastAPI backend)

---

## 📌 Overview

Smart Contract Summary & Q&A Assistant allows users to upload long documents,
ask precise questions, and receive answers strictly grounded in the document
content with page-level citations and automatic evaluation.

The system includes strong guardrails to prevent hallucinations and an
LLM-based evaluator to score answer quality and compliance.

---

## 🎯 Key Capabilities

- Upload and index PDF & DOCX documents
- Page-aware parsing using [[PAGE X]] tagging
- Semantic chunking with overlap
- Vector similarity search using Chroma
- Context-only question answering
- Strict anti-hallucination guardrails
- Conversation memory
- Automatic answer evaluation
- Single & batch evaluation
- Local microservice architecture
- Interactive Gradio UI

---

## 🧠 RAG + Evaluation Pipeline

Question Answering Flow:
1. User uploads documents (PDF / DOCX)
2. Documents are split into semantic chunks
3. Embeddings are generated using Sentence Transformers
4. Chunks are stored in a Chroma vector database
5. Relevant chunks are retrieved via similarity search
6. LLM generates answers strictly from retrieved context
7. Answers include page-level citations

Evaluation Flow:
- Answer Accuracy
- Faithfulness to Context
- Citation Accuracy
- Guard-Rail Compliance
- Overall Performance Score

Evaluation can be applied to:
- The last response
- The last N responses (batch mode)

---

## 🏗 System Architecture
```
User
↓
Gradio UI (app.py)
- Document upload & indexing
- Chat interface
- Evaluation trigger
↓
FastAPI Backend (server_app.py)
- RAG answer chain
- Evaluation chain
↓
LLM (HuggingFace Inference API)
```
---

## 🖥 Frontend (app.py)

- Interactive Gradio chat UI
- Multi-file upload (PDF / DOCX)
- Indexing status display
- On-demand evaluation
- Communicates with FastAPI backend

---

## ⚙ Backend (server_app.py)

Endpoints:
- /rag_chat        → RAG-based question answering
- /evaluate_local  → Evaluate single or combined answers
- /evaluate_batch  → Batch evaluation

Enforced rules:
- Context exclusivity
- No external knowledge
- No hallucinations
- Explicit conflict reporting
- Page-based citations

---

## 🛠 Technology Stack

Backend API: FastAPI  
RAG Framework: LangChain  
Frontend: Gradio  
Vector Store: Chroma  
Embeddings: sentence-transformers/all-MiniLM-L6-v2  
LLM Provider: HuggingFace Inference API  
LLM Model: LLaMA 3.1 8B Instruct  
Document Loaders: PyMuPDF, Unstructured  
Evaluation: LLM-based RAG evaluator  
Environment Management: python-dotenv  

---

## 📂 Project Structure
```
Smart-Contract-Summary-Q-A-Assistant/
├── app.py
├── server_app.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```
---

### ⚙ Installation

## 1️⃣ Clone the repository
```
git clone https://github.com/fares-ahmed7/Smart-Contract-Summary-Q-A-Assistant.git
cd Smart-Contract-Summary-Q-A-Assistant
```

## 2️⃣ Create Virtual Environment
```
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows
```

## 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

## 4️⃣ Configure Environment Variables
Create .env file:
```
HF_TOKEN=your_huggingface_token_here
```
---

### ▶️ Running the Project

## 1️⃣ Start backend server
```
uvicorn server_app:app --host 127.0.0.1 --port 9017
```
## 2️⃣ Start the Frontend (Gradio UI) 
(in another terminal):
```Bash
python app.py
```
The Gradio interface will open automatically in your browser.

---

## 📈 Evaluation Metrics

- Answer Accuracy
- Faithfulness to Context
- Citation Accuracy
- Guard-Rail Compliance
- Overall Performance Score

---

## 🧑‍💻 Author

Fares Ahmed
AI / ML Engineer

---

## 🧑‍💻 Author
**Fares Ahmed**  
AI/ML Engineer
