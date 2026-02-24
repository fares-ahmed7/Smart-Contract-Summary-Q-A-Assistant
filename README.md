# 🚀 Smart Contract Summary & Q&A Assistant (RAG + Evaluation)

## 📌 Overview
**Smart Contract Summary & Q&A Assistant** is a local Retrieval-Augmented Generation (RAG) system with a built-in evaluation framework. 
It allows users to upload long documents (PDF/DOCX), ask precise questions, and receive answers strictly grounded in the document content, complete with **page-level citations** and **automatic quality scoring**.

The system is designed with **strong guardrails** to prevent hallucinations and includes an **LLM-based evaluator** to score answer accuracy, faithfulness, and compliance.

---

## 🎯 Key Capabilities
* ✅ **Multi-format Ingestion:** Upload and index PDF & DOCX documents.
* ✅ **Page-aware Parsing:** Automatic [[PAGE X]] tagging for precise citations.
* ✅ **Semantic Chunking:** Advanced text splitting with overlap for context retention.
* ✅ **Vector Search:** High-performance similarity search using ChromaDB.
* ✅ **Anti-Hallucination:** Strict system prompts ensuring context exclusivity.
* ✅ **Built-in Evaluation:** Automatic scoring for Accuracy, Faithfulness, and Citations.
* ✅ **Local Microservice:** Powered by FastAPI and LangServe.
* ✅ **Interactive UI:** Clean Gradio interface for seamless chat experience.

---

## 🧠 System Pipeline

### 🔹 Question Answering Flow
1. **Ingestion:** Documents are parsed and split into semantic chunks.
2. **Embedding:** Chunks are converted to vectors using `sentence-transformers`.
3. **Retrieval:** Relevant context is fetched from ChromaDB based on user query.
4. **Generation:** LLaMA 3.1 8B generates an answer based *only* on retrieved context.

### 🔹 Evaluation Metrics (LLM-as-a-Judge)
After answering, the system evaluates the response using:
* **Answer Accuracy:** Does it answer the user's intent?
* **Faithfulness:** Is the answer derived solely from the provided context?
* **Citation Accuracy:** Are the page numbers correct?
* **Guard-Rail Compliance:** Did the model follow safety/exclusion rules?

---

## 📂 Project Structure
```
Smart-Contract-Summary-Q-A-Assistant/
├── server_app.py      # FastAPI backend + RAG & Evaluation chains
├── app.py             # Gradio UI (Frontend)
├── .gitignore         # Excludes local storage, env files, and cache
├── requirements.txt   # Project dependencies
└── README.md          # Documentation
```

---

## 🛠 Technology Stack

| Category       | Tool                                             |
|----------------|-------------------------------------------------|
| Backend API    | FastAPI + LangServe                              |
| RAG Framework  | LangChain                                        |
| Frontend       | Gradio                                           |
| Vector Store   | ChromaDB                                         |
| Embeddings     | sentence-transformers/all-MiniLM-L6-v2          |
| LLM Model      | LLaMA 3.1 8B Instruct (via HF Inference API)   |

---

## 2️⃣ Environment Setup

```bash
python -m venv .venv
# Activate:
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

---

## 3️⃣ Configuration
Create a `.env` file in the root directory:
```env
HF_TOKEN=your_huggingface_token_here
```

---

## ▶️ Running the Application

### Step 1: Start Backend Server
```bash
uvicorn server_app:app --host 127.0.0.1 --port 9017
```

### Step 2: Launch Frontend (Gradio)
In a separate terminal, run:
```bash
python app.py
```
The Gradio interface will open in your browser automatically.

---

## 🧑‍💻 Author
**Fares Ahmed**  
AI/ML Engineer
