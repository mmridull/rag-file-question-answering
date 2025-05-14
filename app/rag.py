
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
USE_REAL_API = False

import fitz  # PyMuPDF
from docx import Document
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

chunks = []

def process_file(filepath):
    global chunks
    text = ""
    if filepath.endswith(".pdf"):
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
    elif filepath.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    elif filepath.endswith(".docx"):
        doc = Document(filepath)
        text = " ".join([para.text for para in doc.paragraphs])

    else:
        text = "Unsupported file format."

    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

USE_REAL_API = False  # Change to True when you have quota again

def answer_query(question):
    if not chunks:
        return "No content to search from. Please upload a file first."

    context = "\n\n".join(chunks[:5])
    prompt = f"Answer the following question based on the context:\n\n{context}\n\nQuestion: {question}"

    if USE_REAL_API:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
    else:
        return f"[Simulated Answer] Here's a mock response for your question: '{question}'"

