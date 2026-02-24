import os, time, subprocess, sys
import gradio as gr
from langserve import RemoteRunnable
from langchain_community.document_loaders import PyMuPDFLoader, UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, AIMessage
import requests
import json
import re

PORT = 9017
document_store = None
chat_history = []

if sys.platform == "win32":
    os.system(f'for /f "tokens=5" %a in (\'netstat -aon ^| findstr :{PORT}\') do taskkill /f /pid %a > nul 2>&1')
else:
    os.system(f"fuser -k {PORT}/tcp > /dev/null 2>&1")

time.sleep(2)
subprocess.Popen([sys.executable, "server_app.py"])
print("🚀 Initializing Assistant... (15s)")
time.sleep(15)

chat_client = RemoteRunnable(f"http://127.0.0.1:{PORT}/rag_chat/")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def extract_text(item):
    if isinstance(item, str): return item
    if hasattr(item, 'content'): return item.content
    if isinstance(item, dict): return item.get("text", str(item))
    return str(item)

def convert_history(history):
    messages = []
    for item in history:
        if isinstance(item, (list, tuple)) and len(item) == 2:
            u = extract_text(item[0])
            a = extract_text(item[1])
            if u: messages.append(HumanMessage(content=u))
            if a: messages.append(AIMessage(content=a))
    return messages

def safe_format_eval_output(raw_text: str) -> str:
    if not raw_text:
        return "⚠️ Empty evaluation result."
    try:
        parsed = json.loads(raw_text)
        if isinstance(parsed, dict):
            return "\n".join(f"{k}: {v}" for k, v in parsed.items())
    except json.JSONDecodeError:
        try:
            match = re.search(r"\{[\s\S]*\}", raw_text)
            if match:
                parsed = json.loads(match.group())
                return "\n".join(f"{k}: {v}" for k, v in parsed.items())
        except:
            pass
    return raw_text

def process_files(files):
    global document_store
    if not files: return "No files uploaded."
    all_docs = []
    try:
        for file in files:
            loader = PyMuPDFLoader(file.name) if file.name.lower().endswith('.pdf') else UnstructuredWordDocumentLoader(file.name)
            pages = loader.load()
            for i, page in enumerate(pages):
                page.metadata["page"] = i + 1
                page.page_content = f"[[PAGE {i+1}]] {page.page_content}"
                all_docs.append(page)

        document_store = Chroma.from_documents(
            RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=250).split_documents(all_docs),
            embeddings
        )

        return f"✅ READY: {len(all_docs)} pages indexed."
    except Exception as e:
        return f"❌ Ingestion Error: {str(e)}"

def chat_engine(message, history):
    global document_store, chat_history
    if document_store is None:
        return "⚠️ Please upload documents first."

    msg_text = extract_text(message)

    try:
        docs = document_store.similarity_search(msg_text, k=5)
        context_text = "\n\n".join([d.page_content for d in docs])

        response = chat_client.invoke({
            "question": msg_text,
            "context": context_text,
            "chat_history": convert_history(chat_history)
        })

        chat_history.append([msg_text, response])
        return response

    except Exception as e:
        return f"❌ AI Error: {str(e)}"

def evaluate_last_n_responses(n: int):
    global chat_history, document_store
    if not chat_history:
        return "⚠️ No AI responses yet."

    q = extract_text(chat_history[-1][0])
    a = extract_text(chat_history[-1][1])

    docs = document_store.similarity_search(q, k=3)
    context_text = "\n".join([d.page_content for d in docs])

    try:
        r = requests.post(
            f"http://127.0.0.1:{PORT}/evaluate_local/",
            json={
                "question": q,
                "answer": a,
                "context": context_text
            }
        )

        data = r.json()
        if "error" in data:
            return data["error"]

        return "\n".join([f"⭐ {k}: {v}" for k, v in data.items()])

    except Exception as e:
        return f"❌ Eval Error: {str(e)}"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 Smart Contract Summary & Q&A Assistant")

    with gr.Row():
        file_in = gr.File(label="Upload PDF/DOCX", file_count="multiple")
        status = gr.Textbox(label="System Status", interactive=False)

    file_in.change(process_files, file_in, status)

    chat_ui = gr.ChatInterface(fn=chat_engine)

    with gr.Row():
        n_input = gr.Number(label="Number of Messages to Evaluate", value=1)
        eval_output = gr.Textbox(label="Evaluation Result", interactive=False)
        eval_button = gr.Button("Evaluate AI Responses")

    eval_button.click(
        evaluate_last_n_responses,
        inputs=[n_input],
        outputs=[eval_output]
    )

demo.launch()