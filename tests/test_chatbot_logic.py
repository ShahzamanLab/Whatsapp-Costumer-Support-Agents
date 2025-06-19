import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    st.error("❌ GROQ_API_KEY is missing from environment variables")
    st.stop()


@st.cache_resource(show_spinner="Initializing AI Assistant...")
def setup_qa_system():
    
    try:
        loader = TextLoader("data/faqs.txt", encoding='utf-8')
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", ". ", "! ", "? ", " ", ""]
        )
        docs = text_splitter.split_documents(documents)
    except Exception as e:
        st.error(f"📄 Failed to load documents: {str(e)}")
        st.stop()

    
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )
        
        vectorstore = FAISS.from_documents(docs, embeddings)
    except Exception as e:
        st.error(f"🔍 Vector store initialization failed: {str(e)}")
        st.stop()

    
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

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=False  
    )


st.set_page_config(
    page_title="Phymaco AI Assistant",
    page_icon="💊",
    layout="centered"
)


st.markdown("""
<style>
    .stTextInput input {
        border-radius: 20px;
        padding: 12px 15px;
    }
    .stChatMessage {
        padding: 12px 16px;
    }
</style>
""", unsafe_allow_html=True)

st.title("💊 Phymaco Smart Assistant")
st.caption("Your intelligent pharmaceutical companion")


if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Hello! I'm Phymaco's AI assistant. I can help with medication information, company services, and general pharmaceutical advice."
    }]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask about Phymaco's products or services..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            qa = setup_qa_system()
            with st.spinner("Analyzing your question..."):
                response = qa({"query": prompt})
            
            
            st.markdown(response["result"])
            st.session_state.messages.append({
                "role": "assistant",
                "content": response["result"]
            })
            
        except Exception as e:
            st.error("Our systems are busy. Please try again shortly.")
            st.session_state.messages.append({
                "role": "assistant",
                "content": "I'm currently experiencing high demand. Could you please rephrase your question about Phymaco?"
            })


with st.sidebar:
    if st.button("🧹 Clear Conversation"):
        st.session_state.messages = [{
            "role": "assistant",
            "content": "How can I help you with Phymaco's pharmaceutical services today?"
        }]
        st.rerun()
    
    st.divider()
    st.caption("Phymaco AI v2.1")
    st.caption("Always provide company-relevant information")