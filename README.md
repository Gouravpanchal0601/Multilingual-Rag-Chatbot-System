# 🌐 Multilingual RAG Chatbot

A Multilingual **RAG-based Chatbot** supporting multiple languages for global investor communications.  
Built with cutting-edge NLP tools to provide accurate, multilingual Q&A on investor documents.

---

## 🚀 Features

- **Multilingual Support**: Handles queries in any language using language detection with LangDetect.  
- **Document Ingestion & Chunking**: Parses PDFs via **pdfplumber** and splits them for efficient retrieval.  
- **Vector Search**: Uses **FAISS** for persistent vector storage and semantic search.  
- **RAG-powered Responses**: Answers user queries using **OpenAI LLMs** enhanced by retrieved document chunks.  
- **CLI-based Interface**: Lightweight, terminal-based interface for quick investor Q&A.  

---

## 🛠️ Tech Stack

- **pdfplumber** - PDF parsing and text extraction  
- **FAISS** - High-performance vector database for semantic search  
- **LangDetect** - Automatic language detection  
- **OpenAI API** - LLM-powered answers  
- **RAG (Retrieval-Augmented Generation)** - Combines vector search with LLM generation  

---

## 💻 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Gouravpanchal0601/Multilingual-Rag-Chatbot-System
    cd multilingual-ir-chatbot
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the chatbot CLI:
    ```bash
    python main.py
    ```
---

## ⚙️ Usage

- Place your investor PDF documents in the `/docs` folder.  
- The chatbot will ingest, chunk, and embed them automatically.  
- Ask questions in **any language**, and the bot will retrieve relevant info and respond:  

---

## 🤝 Contributions

Contributions, suggestions, and improvements are welcome! Feel free to open an issue or submit a pull request.

---

## 📬 Contact

For any questions or collaborations:  
**Email:** [Gourav Panchal - Mail](gourav.panchal0601@gmail.com)  
**GitHub:** [Gourav Panchal - Github](https://github.com/Gouravpanchal0601)

---

**Made with ❤️ using OpenAI, LangChain, LangGraph, RAG System, LangSmith and Streamlit**
