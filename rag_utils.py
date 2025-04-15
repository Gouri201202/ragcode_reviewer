import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA

def embed_documents(directory):
    loader = TextLoader(os.path.join(directory, 'buggy_code.py'))
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    return db

def review_code(code_snippet: str) -> str:
    # Dummy review for testing
    return "This code has a few syntax issues and lacks proper error handling."

def fix_code(code_snippet: str) -> str:
    # Dummy fixed code for testing
    return code_snippet.replace("pritn", "print")  # Example fix

def generate_review_and_fix(code_snippet: str):
    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Generate review and fix
    review = review_code(code_snippet)
    fixed_code = fix_code(code_snippet)

    # Save review to output/review.txt
    with open("output/review.txt", "w", encoding="utf-8") as review_file:
        review_file.write(review)

    # Save fixed code to output/fixed_code.txt
    with open("output/fixed_code.txt", "w", encoding="utf-8") as code_file:
        code_file.write(fixed_code)

    return review, fixed_code
