import gradio as gr

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

CHROMA_PATH = "chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    encode_kwargs={
        "normalize_embeddings": True
    }
)

vector_store = Chroma(
    collection_name="traffic_law",
    embedding_function=embedding_model,
    persist_directory=CHROMA_PATH
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)

llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0.1
)

def answer_question(message, history):

    docs = retriever.invoke(message)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    prompt = f"""
คุณเป็นผู้ช่วยตอบคำถามจากเอกสาร

ข้อมูลอ้างอิง:

{context}

คำถาม:
{message}

ตอบจากข้อมูลอ้างอิงเท่านั้น
หากไม่มีข้อมูลให้ตอบว่า
"ไม่พบข้อมูลในเอกสาร"
"""

    response = ""

    for chunk in llm.stream(prompt):
        response += chunk.content
        yield response

demo = gr.ChatInterface(
    fn=answer_question,
    title="Traffic Law RAG",
    description="ถามตอบเรื่องกฏหมายจราจร"
)

demo.launch()