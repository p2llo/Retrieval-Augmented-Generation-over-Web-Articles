# **Retrieval-Augmented Generation (RAG) Web Article Chatbot**  
**A Streamlit + LangChain + Mistral AI application for querying web articles using RAG.**  

## **📌 Overview**  
This project implements a **Retrieval-Augmented Generation (RAG)** system that:  
1. **Loads** a web article from a given URL.  
2. **Processes & Splits** the text into chunks.  
3. **Generates Embeddings** using HuggingFace's BGE model.  
4. **Stores** them in a Chroma vector database.  
5. **Answers questions** using Mistral AI's LLM with document retrieval.  

The frontend is built with **Streamlit**, providing an interactive chat interface.  

---

## **🚀 Features**  
✔ **Web Article Retrieval** – Extract and process content from any URL.  
✔ **Chunking & Embeddings** – Splits text into manageable chunks and generates embeddings.  
✔ **Vector Search** – Uses ChromaDB for efficient document retrieval.  
✔ **Chat Interface** – Streamlit-powered UI for interactive Q&A.  
✔ **Mistral AI Integration** – Leverages `mistral-large-latest` for high-quality responses.  

---

## **🛠 Setup & Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **2. Create & Activate a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Set Up Mistral API Key**  
Replace `your-api-key` in `langchain_helper.py` with your actual [Mistral AI API key](https://console.mistral.ai/).  

---

## **💻 Usage**  
1. **Run the Streamlit App**  
   ```bash
   streamlit run main.py
   ```
2. **Enter a URL** in the sidebar.  
3. **Ask questions** in the chat interface.  

Example:  
- **URL:** `https://en.wikipedia.org/wiki/Large_language_model`  
- **Question:** *"What are the key applications of LLMs?"*  

---

## **📂 Project Structure**  
```
├── main.py                # Streamlit UI & chat logic  
├── langchain_helper.py    # LangChain RAG pipeline  
├── requirements.txt       # Python dependencies  
└── README.md              # This file  
```

---

## **🔧 Dependencies**  
- `streamlit` – Web UI  
- `langchain` – RAG pipeline  
- `mistralai` – Mistral LLM integration  
- `chromadb` – Vector storage  
- `unstructured` – Web document loading  
- `huggingface-hub` – Embeddings  

---


### **🎉 Happy Querying!** 🎉  
Deploy this to **Hugging Face Spaces** or **Streamlit Cloud** for easy sharing! 🚀  

---

**🔗 Related Projects:**  
- [LangChain Documentation](https://python.langchain.com/)  
- [Mistral AI API](https://docs.mistral.ai/)  
- [ChromaDB Guide](https://docs.trychroma.com/)  

---
