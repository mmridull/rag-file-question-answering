# 🧠 RAG File-Based Question Answering App (Flask)

This project is an end-to-end Retrieval-Augmented Generation (RAG) system that allows users to:

📁 Upload any `.pdf`, `.docx`, or `.txt` file  
❓ Ask questions about the uploaded content  
🤖 Get answers (from OpenAI API or simulated responses)

Built using **Python**, **Flask**, and **LangChain**, this app demonstrates local document ingestion and Q&A without requiring cloud storage.

---

## 🚀 Features

- Upload documents and extract text automatically
- Chunk and embed document content
- Ask natural language questions about the uploaded file
- Switch between **real OpenAI API** or **simulated mock responses**
- Clean frontend using basic HTML (no JS or Node required)

---

## 🛠 Tech Stack

- Python 3.9+
- Flask
- LangChain
- OpenAI API
- FAISS (in-memory vector store)
- PDF, DOCX, TXT parsing
- HTML + Bootstrap (optional)

---

## 📂 Folder Structure

rag_project_flat/
├── app/
│ ├── main.py # Flask backend
│ ├── templates/
│ │ └── index.html # Upload UI and question form
├── rag.py # Core logic: parsing, chunking, querying
├── requirements.txt # Python dependencies
├── .env # Stores your OpenAI API key (not uploaded)
├── .gitignore # Prevents uploading venv/.env
├── README.md # This file!
└── venv/ # Your local virtual environment


---

## 🧪 Local Setup

### 1. Clone this repo

```bash
git clone https://github.com/your-username/rag-file-question-answering.git
cd rag-file-question-answering
python -m venv venv
venv\Scripts\activate       # On Windows
# or
source venv/bin/activate    # On macOS/Linux

pip install -r requirements.txt

add openai key

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

python app/main.py
