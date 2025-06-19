import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


load_dotenv()


loader = TextLoader("data/faqs.txt", encoding='utf-8')
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ". ", "! ", "? ", " ", ""]
)
docs = text_splitter.split_documents(documents)


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)


vectorstore = FAISS.from_documents(docs, embeddings)


llm = ChatGroq(
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.4,
    max_tokens=1024
)


prompt_template = """
You are Phymaco's intelligent pharmaceutical assistant. Your responses should:
- Be professional, helpful and company-focused
- Use the context when available
- When context is missing, provide a smart, relevant response about Phymaco
- Never say "I don't know" - instead offer related information

Context: {context}

Question: {question}

Phymaco-focused Answer:
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)


qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=False
)


def get_response(user_query: str) -> str:
    result = qa.invoke({"query": user_query})
    return result["result"]
