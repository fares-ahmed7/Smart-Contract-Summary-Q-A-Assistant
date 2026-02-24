import os
import time
import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Smart Contract Assistant Server",
    description="AI server for Smart Contract Q&A with evaluation",
    version="1.0.0"
)

llm = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
    model="meta-llama/Llama-3.1-8B-Instruct:novita",
    temperature=0.3,
    max_tokens=1000
)

system_instruction = """
You are a professional Document Q&A Assistant. Your goal is to provide high-fidelity information strictly extracted from the provided context.

CRITICAL RULES:
1. EXCLUSIVITY: Answer ONLY using the provided CONTEXT. If the information is not in the text, state: "I cannot find this information in the document."
2. CONFLICT RESOLUTION: If the document contains conflicting information (e.g., different titles for the same chapter or mismatched page numbers), you MUST report all versions found and explicitly mention the discrepancy. Do NOT try to 'fix' or 'logicize' the author's mistakes.
3. NO EXTERNAL KNOWLEDGE: Do not use internal knowledge to define terms or solve equations. If a term like 'Singular Solution' is not defined in the text, do not define it.
4. FACTUAL INTEGRITY: Never guess or invent page numbers. 
5. MATH & SYMBOLS: 
   - Extract mathematical formulas as clearly as possible. 
   - If a formula looks cluttered or broken in the raw text, reformat it into a readable standard (e.g., dy/dx = f(x)).
   - Use LaTeX format for complex equations using $inline$ or $$display$$ symbols.

CITATION & OUTPUT FORMAT:
- Direct Answer: [Detailed answer based strictly on context]
- Sources: Always use the format [Page X]. If the information appears on multiple pages, list them all.

GREETINGS & IDENTITY:
- Briefly and politely acknowledge greetings.
- Identity: "I am an AI Document Assistant designed to answer questions strictly based on your uploaded files."

CONTEXT:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_instruction),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

EVAL_PROMPT = """You are an expert evaluator for RAG systems.
Given a QUESTION, the CONTEXT, and the GENERATED ANSWER,
evaluate the answer and provide a JSON object containing the following metrics:

- Answer Accuracy (percentage, 0-100%)
- Faithfulness (percentage, 0-100%)
- Citation Accuracy (percentage, 0-100%)
- Score (percentage, 0-100%)
- Guard-Rail Compliance (percentage, 0-100%)
- Overall Performance (score out of 10)

Respond ONLY with valid JSON in this exact format:

{{
    "Answer Accuracy": "~{{answer_accuracy}}%",
    "Faithfulness": "~{{faithfulness}}%",
    "Citation Accuracy": "~{{citation_accuracy}}%",
    "Score": "~{{score}}%",
    "Guard-Rail Compliance": "~{{guard_rail}}%",
    "Overall Performance": "{{overall}}/10"
}}

QUESTION: {question}
CONTEXT: {context}
ANSWER: {answer}
"""

eval_prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are a precise RAG evaluator. Output ONLY valid JSON.'),
    ('human', EVAL_PROMPT)
])

chain = prompt | llm | StrOutputParser()
eval_chain = eval_prompt | llm | StrOutputParser()

add_routes(app, chain, path="/rag_chat")
add_routes(app, eval_chain, path="/evaluate")

class EvalRequest(BaseModel):
    question: str
    answer: str
    context: str

class EvalBatchRequest(BaseModel):
    history: List[dict]

@app.post("/evaluate_local/")
def evaluate_local(request: EvalRequest):
    try:
        result = eval_chain.invoke({
            "question": request.question,
            "answer": request.answer,
            "context": request.context
        })

        parsed = json.loads(result)

        return JSONResponse(content=parsed)

    except Exception as e:
        return {"error": f"Eval Chain Error: {str(e)}"}

@app.post("/evaluate_batch/")
def evaluate_batch(request: EvalBatchRequest):
    results = []
    for item in request.history:
        try:
            result = eval_chain.invoke({
                "question": item["question"],
                "answer": item["answer"],
                "context": item["context"]
            })
            try:
                parsed = json.loads(result)
                results.append(parsed)
            except:
                results.append({"raw_result": result})
        except Exception as e:
            results.append({"error": str(e)})
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9017)
