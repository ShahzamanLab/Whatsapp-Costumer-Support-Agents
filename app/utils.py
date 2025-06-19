import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

def load_documents(file_path: str):
    loader = TextLoader(file_path, encoding='utf-8')
    return loader.load()

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", "! ", "? ", " ", ""]
    )
    return splitter.split_documents(documents)

def create_embeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", device="cpu"):
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": device}
    )

def build_vectorstore(docs, embeddings):
    return FAISS.from_documents(docs, embeddings)

def get_env_var(key: str, default=None):
    return os.getenv(key, default)

def clean_text(text: str):
    return text.strip().lower()
