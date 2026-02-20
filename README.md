# 🚀 Smart Contract Summary & Q&A Assistant (RAG + Evaluation)

## 📌 Overview

Smart Contract Summary & Q&A Assistant is a **local Retrieval-Augmented Generation (RAG) system with built-in evaluation**.  
It allows users to upload long documents (PDF / DOCX), ask precise questions, and receive **answers strictly grounded in the document content**, with **page-level citations** and **automatic answer quality evaluation**.

The system is designed with **strong guardrails** to prevent hallucinations and includes an **LLM-based evaluator** to score answer accuracy, faithfulness, citation correctness, and guard-rail compliance.

---

## 🎯 Key Capabilities

✅ Upload and index PDF & DOCX documents  
✅ Page-aware document parsing (`[[PAGE X]]` tagging)  
✅ Semantic chunking with overlap  
✅ Vector similarity search using embeddings  
✅ Context-grounded Q&A (no external knowledge)  
✅ Strict anti-hallucination guardrails  
✅ Conversation memory support  
✅ Automatic RAG answer evaluation  
✅ Batch and single-response evaluation  
✅ Local microservice architecture (FastAPI + LangServe)  
✅ Interactive Gradio chat UI  

---

## 🧠 RAG + Evaluation Pipeline

### 🔹 Question Answering Flow

1. User uploads documents (PDF / DOCX)
2. Documents are split into semantic chunks
3. Embeddings are generated using Sentence Transformers
4. Chunks are stored in a Chroma vector database
5. Relevant chunks are retrieved via similarity search
6. LLM generates answers **strictly from retrieved context**
7. Answers include page-level references

---

### 🔹 Evaluation Flow (RAG Metrics)

After answering, the system can evaluate responses using an **LLM-based evaluator**:

- Answer Accuracy
- Faithfulness to Context
- Citation Accuracy
- Guard-Rail Compliance
- Overall Performance Score

Evaluation can be applied to:
- The last response
- The last *N* responses (batch mode)

---

## 🏗 System Architecture
User
 │
 ▼
Gradio UI (Frontend)
 │
 ├── Document Upload & Parsing
 │
 ├── Vector Search (Chroma)
 │
 ▼
FastAPI Backend (LangServe)
 │
 ├── RAG Answer Chain
 │
 └── Evaluation Chain
 │
 ▼
LLM (HuggingFace Inference API)

---

## 🖥 Frontend (Gradio)

- Interactive chat interface
- Multi-file upload (PDF / DOCX)
- Document indexing status display
- On-demand evaluation button
- Automatic backend startup

---

## ⚙ Backend (FastAPI + LangServe)

- `/rag_chat` → RAG-based question answering
- `/evaluate_local` → Evaluate single or combined answers
- `/evaluate_batch` → Batch evaluation support
- Strict system prompt enforcing:
  - Context exclusivity
  - No hallucination
  - Explicit conflict reporting
  - Page-based citations

---

## 🛠 Technology Stack

| Category | Tool |
|-------|------|
| Backend API | FastAPI |
| RAG Framework | LangChain + LangServe |
| Frontend | Gradio |
| Vector Store | Chroma |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| LLM Provider | HuggingFace Inference API |
| LLM Model | LLaMA 3.1 8B Instruct |
| Document Loaders | PyMuPDF, Unstructured |
| Evaluation | LLM-based RAG Evaluator |
| Env Management | python-dotenv |

---

## 📂 Project Structure
```
Smart-Contract-Summary-Q-A-Assistant
│
├── server_app.py # FastAPI backend + RAG & evaluation chains
├── frontend.py # Gradio UI + document pipeline
├── chroma_db_storage/ # Vector database persistence
├── .env # HuggingFace API token
├── requirements.txt # Dependencies
└── README.md # Documentation
```

---

## ⚙ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/fares-ahmed7/Smart-Contract-Summary-Q-A-Assistant.git
cd Smart-Contract-Summary-Q-A-Assistant
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_token
```

---

## ▶️ Running The Project

### Start Backend Server

```
uvicorn server_app:app --host 127.0.0.1 --port 9017
```

---

### ▶️ Running the Application
🚀 Start the System (Recommended)
```bash
python frontend.py
```

✔ Automatically launches the backend
✔ Starts the Gradio interface
✔ Opens the chat UI in your browser
---

## 📈 Evaluation Metrics

The system evaluates generated answers using an LLM-based evaluator with the following metrics:
- Answer Accuracy
- Faithfulness to Context
- Citation Accuracy
- Guard-Rail Compliance
- Overall Performance Score
