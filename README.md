# Traffic Law AI Advisor
---
# โหลดโปรเจค
clone โปรเจค

        git clone https://github.com/nattaken/Traffic-Law-Advisor.git
หรือ โหลด zip file โปรเจค

---
# ดาวน์โหลดโมเดล
        ollama pull llama3.2
หากยังไม่มีโมเดลให้เข้าไปติดตั้ง ollama ก่อน

        https://ollama.com/download/windows
---
# สร้าง Virtual Environment
        python -m venv venv
เปิดใช้งาน

        venv\Scripts\activate
---
# ติดตั้ง Library
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
# โครงสร้างโปรเจค

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

4. หลังจากได้ vector database ก็ทำการรันไฟล์ app.py ที่จะเป็นตัวเว็บแชท

  *** หลังจากได้ vector database สามารถลบไฟล์ build_db.py และ โฟลเดอร์ data ได้ ***
5. 


6. -
