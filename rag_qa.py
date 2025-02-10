import os
import ollama
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP, FAISS_INDEX_PATH

embeddings = HuggingFaceEmbeddings()

def process_pdf(pdf_path):
    loader = UnstructuredFileLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = CharacterTextSplitter(separator="\n",chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)
    text_chunks = text_splitter.split_documents(documents)
    
    knowledge_base = FAISS.from_documents(text_chunks, embeddings)
    
    return knowledge_base

def retrieval(user_query, knowledge_base):
    if not os.path.exists(FAISS_INDEX_PATH):
        return "No documents processed yet. Please upload a PDF."
    
    retriever = knowledge_base.as_retriever(search_kwargs={"k": 3})
    retrieved_chunks = retriever.invoke(user_query)
    retrieved_data = "\n".join([doc.page_content for doc in retrieved_chunks])
    
    prompt = f"""
        ### Context:
        {retrieved_data}
        ### Query:
        {user_query}
        ### Answer:
    """
    
    response = ollama.chat(model="llama3.2:1b", messages=[{"role": "user", "content": prompt}])
    
    return response["message"]["content"]
    