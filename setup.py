from setuptools import setup, find_packages

setup(
    
    name="Costumer_Support_Whatsapp_Chatbot",
    version="1.0.0",
    author="Shahzaman",
    author_email="gallanizaman@gmail.com",
    description="""AI Whatsapp Costumer Support chatbot that give the response of the query 
    as company provided data it work more better then human and improve the response time
    it is 100 time faster then human and use llm to give support response.""",
    long_description=open("README.md").read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "langchain-core",
        "langchain-community",
        "langchain-groq",
        "langchain-huggingface",
        "twilio",
        "python-dotenv",
        "python-multipart",
        "streamlit",
        "transformers",
        "sentence-transformers",
        "faiss-cpu",
        "pyngrok",
        "numpy",
        "pandas"
    ],
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "Operating System :: OS Independent",
    ],
    
    python_requires='>=3.8',


    
)