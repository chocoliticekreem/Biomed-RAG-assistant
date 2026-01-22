import sqlite3 as sq
import pdfplumber
import streamlit as st
import os
from llama_index.core import Document, VectorStoreIndex, StorageContext, load_index_from_storage

def start_db():
    with sq.connect('biomeddata.db') as connection:
        conn = connection.cursor()
        conn.execute('''CREATE TABLE IF NOT EXISTS reports
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT,
                      content TEXT)''')

def process_files(file):
    #extract text from PDF
    with pdfplumber.open(file) as pdf:
        extracted_text = ''
        extracted_text += '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())

    #create database
    with sq.connect('biomeddata.db') as connection:
        conn = connection.cursor()
        conn.execute("""INSERT INTO reports (title, content) VALUES (?, ?)""", (file.name, extracted_text))
    #vector index for RAG
    doc = Document(text=extracted_text, metadata={"title": file.name})

    if not os.path.exists(os.path.join('./index_storage', 'docstore.json')):
        index = VectorStoreIndex.from_documents([doc])
    else:
        storage_context = StorageContext.from_defaults(persist_dir='./index_storage')
        index = load_index_from_storage(storage_context)
        index.insert(doc)
    index.storage_context.persist(persist_dir='./index_storage')
    return index 




