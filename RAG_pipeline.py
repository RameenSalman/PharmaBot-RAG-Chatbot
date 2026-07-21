import os
from dotenv import load_dotenv

import pandas as pd
from huggingface_hub import login
from langchain_community.document_loaders import TextLoader, UnstructuredExcelLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Hugging Face Login
login(os.getenv("HF_TOKEN"))

# Load the text file
text_loader = TextLoader("policy.txt")
text_documents = text_loader.load()

# Load the Excel file
excel_loader = UnstructuredExcelLoader("products.xlsx")
excel_documents = excel_loader.load()

# Combine all loaded documents
documents = text_documents + excel_documents

# Check the number of loaded documents
print(f"Total documents loaded: {len(documents)}")

# Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Total chunks: {len(chunks)}")

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store embeddings in FAISS
vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

# Retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)