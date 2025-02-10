### **📖 RAG-based Q&A with Ollama & Streamlit**  

A **Retrieval-Augmented Generation (RAG) system** that allows you to **upload PDFs, retrieve relevant chunks, and generate AI-powered answers using Llama 3.2 via Ollama**—all running locally! 🚀  

---

## **📌 Features**  
✅ **PDF Upload & Storage** 📂  
✅ **Text Chunking & FAISS Vector Search** 🔍  
✅ **Retrieve Relevant Information from Documents** 🧩  
✅ **Local AI-Powered Q&A with Llama 3.2 (Ollama)** 🤖  
✅ **Simple UI with Streamlit** 🎛️  

---

## **🛠️ Tech Stack**  
- **Python** 🐍  
- **LangChain** for RAG-based retrieval  
- **FAISS** for vector embeddings  
- **Ollama** for running Llama 3.2 locally  
- **Streamlit** for a lightweight UI  

---

## **🚀 Installation & Setup**  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/abhinavtej/ollama-rag-qa.git
cd ollama-rag-qa
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **4️⃣ Run Ollama Server**
Ensure **Ollama** is installed:  
```bash
ollama serve &
```

### **5️⃣ Start the Streamlit App**
```bash
streamlit run app.py
```

---

## **📂 Project Structure**
```
ollama_rag_qa/
│── venv/                  # Virtual environment
│── uploads/               # Folder to store uploaded PDFs
│── app.py                 # Streamlit frontend
│── rag_qa.py              # Backend processing
│── config.py              # Configuration settings
│── requirements.txt       # Dependencies
│── README.md              # Documentation
│── .gitignore             # Ignore unnecessary files
```

---

## **📌 Usage Guide**
1️⃣ **Upload a PDF** via the Streamlit UI.  
2️⃣ **Ask a question** related to the document.  
3️⃣ The system **retrieves relevant sections** from the PDF.  
4️⃣ **Llama 3.2** generates an answer based on retrieved context.  

---

📢 **Would love to hear your thoughts & suggestions!** Drop a comment or contribute via PRs. 🚀  

---

### **🔗 Connect with Me**
📧 Mail[mailto:abhinavtejreddy.j@gmail.com]  
🔗 Linkedin[www.linkedin.com/in/abhinavtej]  
🐙 Github[www.github.com/abhinavtej]  

---
