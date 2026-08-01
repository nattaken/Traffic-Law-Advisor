# Traffic Law AI Advisor

ระบบถาม-ตอบกฎหมายจราจรไทยจากเอกสาร PDF โดยใช้เทคนิค RAG (Retrieval-Augmented Generation)

## Features

- ค้นหาข้อมูลจากเอกสาร PDF
- ใช้ ChromaDB เป็น Vector Database
- ใช้ BAAI/bge-m3 สำหรับ Embedding
- ใช้ Llama 3.2 ผ่าน Ollama
- มี Web Interface ผ่าน Gradio
- ทำงานแบบ Local ไม่ต้องใช้ API ภายนอก

## System Architecture

ระบบถูกพัฒนาตามแนวคิด Retrieval-Augmented Generation (RAG) โดยนำข้อมูลจากเอกสาร PDF มาแปลงเป็นเวกเตอร์ จัดเก็บในฐานข้อมูลเวกเตอร์ และใช้ Large Language Model ในการสร้างคำตอบจากข้อมูลที่ค้นพบ

```text
  PDF Document
      │
      ▼
  PyPDF Loader
(อ่านข้อมูลจาก PDF)
      │
      ▼
  Text Splitter
(แบ่งเอกสารเป็น Chunk)
      │
      ▼
  BAAI/bge-m3
(สร้าง Embedding Vector)
      │
      ▼
  ChromaDB
(จัดเก็บ Vector Database)
      │
      ▼
  Retriever
(ค้นหา Chunk ที่เกี่ยวข้อง)
      │
      ▼
  Llama 3.2 (Ollama)
(วิเคราะห์และสร้างคำตอบ)
      │
      ▼
  Gradio Interface
(แสดงผลในรูปแบบ Chatbot)
      │
      ▼
     User
```

### Architecture Description

#### 1. PDF Document
เอกสารกฎหมายจราจรในรูปแบบ PDF เป็นแหล่งข้อมูลหลักที่ใช้ในการสร้างฐานความรู้ของระบบ

#### 2. PyPDF Loader
ทำหน้าที่อ่านและดึงข้อความจากไฟล์ PDF เพื่อนำเข้าสู่กระบวนการประมวลผล

#### 3. Text Splitter
แบ่งข้อความขนาดใหญ่ให้เป็นส่วนย่อย (Chunks) เพื่อเพิ่มประสิทธิภาพในการสร้าง Embedding และการค้นคืนข้อมูล

#### 4. BAAI/bge-m3
โมเดล Embedding ที่ใช้แปลงข้อความเป็นเวกเตอร์เชิงตัวเลข เพื่อให้สามารถวัดความคล้ายคลึงระหว่างคำถามและข้อมูลในเอกสารได้

#### 5. ChromaDB
ฐานข้อมูลเวกเตอร์ (Vector Database) ที่ใช้จัดเก็บ Embedding Vector และ Metadata ของเอกสาร เพื่อรองรับการค้นหาแบบ Similarity Search

#### 6. Retriever
ทำหน้าที่ค้นหา Chunk ที่มีความเกี่ยวข้องกับคำถามของผู้ใช้มากที่สุดจาก ChromaDB

#### 7. Llama 3.2 ผ่าน Ollama
Large Language Model (LLM) ที่ใช้วิเคราะห์ข้อมูลจาก Retriever และสร้างคำตอบในรูปแบบภาษาธรรมชาติ

#### 8. Gradio Interface
ส่วนติดต่อผู้ใช้งาน (User Interface) ในรูปแบบ Chatbot สำหรับรับคำถามและแสดงผลลัพธ์

---

## RAG Workflow

```text
 User Question
      │
      ▼
   Retriever
(ค้นหาข้อมูลที่เกี่ยวข้อง)
      │
      ▼
   ChromaDB
(ดึงข้อมูลจากฐานข้อมูลเวกเตอร์)
      │
      ▼
Context + Question
      │
      ▼
   Llama 3.2
(สร้างคำตอบจากข้อมูลที่ค้นพบ)
      │
      ▼
Gradio Chat Interface
      │
      ▼
   Answer
```

### Why RAG?

ระบบนี้ใช้สถาปัตยกรรม Retrieval-Augmented Generation (RAG) ซึ่งเป็นการผสานการค้นคืนข้อมูลจากเอกสาร (Retrieval) เข้ากับความสามารถในการสร้างคำตอบของ Large Language Model (Generation)

แนวทางนี้ช่วยให้ระบบสามารถตอบคำถามโดยอ้างอิงจากข้อมูลจริงภายในเอกสาร ลดปัญหาการสร้างข้อมูลที่ไม่ถูกต้อง (Hallucination) และเพิ่มความน่าเชื่อถือของคำตอบเมื่อเทียบกับการใช้โมเดลภาษาเพียงอย่างเดียว

## เทคโนโลยีที่ใช้

| เทคโนโลยี                                | หน้าที่                                                          |
| ---------------------------------------- | ---------------------------------------------------------------- |
| **Python**                               | ภาษาหลักในการพัฒนาโปรเจกต์                                       |
| **LangChain**                            | Framework สำหรับเชื่อม PDF, Vector Database และ LLM เข้าด้วยกัน  |
| **PyPDF**                                | อ่านและดึงข้อความจากไฟล์ PDF                                     |
| **RecursiveCharacterTextSplitter**       | แบ่งเอกสารเป็น Chunk เพื่อเตรียมสร้าง Embedding                  |
| **BAAI/bge-m3**                          | โมเดล Embedding สำหรับแปลงข้อความเป็นเวกเตอร์                    |
| **HuggingFace**                          | แหล่งที่ใช้ดาวน์โหลดและเรียกใช้โมเดล Embedding                   |
| **ChromaDB**                             | Vector Database สำหรับเก็บ Embedding และค้นหาข้อมูลที่เกี่ยวข้อง |
| **HNSW (HNSWLIB)**                       | อัลกอริทึม Similarity Search ที่ ChromaDB ใช้ภายใน               |
| **Ollama**                               | โปรแกรมสำหรับรัน LLM บนเครื่องแบบ Local                          |
| **Llama 3.2**                            | Large Language Model ที่ใช้สร้างคำตอบ                            |
| **Gradio**                               | Web Interface สำหรับสร้างหน้า Chatbot                            |
| **RAG (Retrieval-Augmented Generation)** | แนวคิดการทำงานที่ผสม Retrieval กับ LLM                           |


# คู่มือการติดตั้ง และการใช้งาน
---
## ติดดั้ง Editor และ Python

ติดตั้ง Editor : Visual Studio Code

ติดตั้งภาษา Python

---
## โหลดโปรเจค
clone โปรเจค

        git clone https://github.com/nattaken/Traffic-Law-Advisor.git
หรือ โหลด zip file โปรเจค

---
## ดาวน์โหลดโมเดล
        ollama pull llama3.2
หากยังไม่มีโมเดลให้เข้าไปติดตั้ง ollama ก่อน

        https://ollama.com/download/windows
---
## สร้าง Virtual Environment
        python -m venv venv
เปิดใช้งาน

        venv\Scripts\activate
---
## ติดตั้ง Library
        pip install gradio
        pip install langchain
        pip install langchain-community
        pip install langchain-chroma
        pip install langchain-huggingface
        pip install langchain-ollama
        pip install chromadb
        pip install sentence-transformers
        pip install torch
        pip install pypdf

---
## โครงสร้างโปรเจค

      project/
      │
      ├── data/
      │   └── กฏหมายจราจร.pdf
      │
      ├── build_db.py
      └── app.py

---
# การใช้งานโปรเจค
หลักจากทำตามขั้นตอนการติดตั้งแล้ว ต่อไปเป็นขั้นตอนการใช้งาน
1. ตรวจสอบว่าในโฟลเดอร์ Data มีไฟล์ กฏหมายจราจร.pdf ที่เป็นไฟล์ข้อมูลหลักหรือไม่
2. ทำการรันไฟล์ build_db.py ซึ่งเป็นโค้ดที่จะทำการแปลงไฟล์ pdf ให้เป็น vector database
3. หลังจากการรัน build_db.py จะมีโฟลเดอร์ใหม่ปรากฎขึ้นชื่อว่าchroma_db ที่เป็น vector database


        project/
        │
        ├── data/
        │   └── traffic_law.pdf
        │
        ├── build_db.py
        ├── app.py
        └── chroma_db/ โฟลเดอร์ใหม่ที่ได้หลังจากการรันไฟล์ build_db.py
   
  ให้ตรวจสอบว่าภายในโฟลเดอร์ chroma_db มีไฟล์ที่ chroma.sqlite3 และโฟลเดอร์ที่ภายในมีไฟล์ 4 ไฟล์นี้
  - data_level0.bin
  - header.bin
  - length.bin
  - link_lists.bin

  
  *** หากไม่เป็นไปตามนี้ ให้ตรวจสอบการติดตั้ง library แล้วรันไฟล์ build_db.py อีกครั้ง ***

4. หลังจากได้ vector database ก็ทำการรันไฟล์ app.py เพื่อเริ่มต้นการใช้งานเว็บแชท
   โดยถ้ารันไฟล์ app.py สำเร็จก็จะแสดงประมาณนี้

        * Running on local URL:  http://127.0.0.1:7860
        * To create a public link, set `share=True` in `launch()`.

สามารถ ctril + click ที่ url หรือ คัดลอก url ไปวางบนเว็บบราวเซอร์

        http://127.0.0.1:7860

  *** หลังจากได้ vector database สามารถลบไฟล์ build_db.py และ โฟลเดอร์ data ได้ ***

---

# หมายเหตุ

สาเหตุที่โปรเจกต์นี้สามารถใช้งานได้เฉพาะบนเครื่อง (Local) เนื่องจากมีการเลือกใช้โมเดล Llama 3.2 ผ่าน Ollama ซึ่งเป็นการรันโมเดลภายในเครื่องผู้ใช้งาน รวมถึงใช้ฐานข้อมูลเวกเตอร์ ChromaDB ที่จัดเก็บอยู่ภายในเครื่องเช่นกัน ทำให้ระบบสามารถทำงานได้โดยไม่ต้องพึ่งพา Cloud API หรือบริการภายนอก เหมาะสำหรับการพัฒนาและทดสอบในรูปแบบ Demo เนื่องจากไม่มีค่าใช้จ่ายในการเรียกใช้งานโมเดล AI ในอนาคตหากพัฒนาไปสู่ระดับ Production อาจมีการปรับเปลี่ยนสถาปัตยกรรมระบบและเลือกใช้โมเดลหรือบริการ LLM ที่เหมาะสมกับการรองรับผู้ใช้งานจำนวนมาก การขยายระบบ และการ Deploy บน Cloud
