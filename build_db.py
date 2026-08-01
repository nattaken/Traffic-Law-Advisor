from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DATA_PATH = "data"
CHROMA_PATH = "chroma_db"

loader = PyPDFDirectoryLoader(DATA_PATH)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"โหลดเอกสาร {len(documents)} หน้า")
print(f"สร้าง Chunk {len(chunks)} ชิ้น")

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

vector_store.add_documents(chunks)

print("สร้าง Vector Database สำเร็จ")