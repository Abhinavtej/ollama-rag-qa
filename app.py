import os
import streamlit as st
from rag_qa import process_pdf, retrieval
from config import UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="RAG Q&A with Ollama", layout="wide")
st.markdown("**_Made with :heart: by [Abhinavtej Reddy](https://www.abhinavtejreddy.me)_**")
st.title("_RAG Q&A_ with :blue[Ollama]")

st.sidebar.header("Upload a PDF")
pdf_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

if pdf_file:
    pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.name)
    with open("uploaded.pdf", "wb") as f:
        f.write(pdf_file.getbuffer())
    st.sidebar.success("File uploaded successfully")
    
    knowledge_base = process_pdf(pdf_path)
    st.sidebar.success("File processed and indexed! ✅")

    st.markdown("Ask Questions from the Document")
    user_query = st.text_input("Enter your question:", "")
    
    if st.button("Ask"):
        if user_query and pdf_file:
            answer = retrieval(user_query, knowledge_base)
            st.write(f"**Answer:** {answer}")
        else:
            st.warning("Please upload a PDF and enter a question.")
        