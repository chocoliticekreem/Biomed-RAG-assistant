import os
#load api key
from dotenv import load_dotenv

from database import start_db, process_files
load_dotenv()

import streamlit as st
import sqlite3 as sq
from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage

#initialize database
start_db()

st.title('Biomed Research Assistant')
st.set_page_config(page_title='Biomed Assistant' , layout='wide')

#create file uploader
with st.sidebar:
    st.header('Upload Biomed Reports/Papers')
    uploaded_file = st.file_uploader('Upload a report/paper', type=['pdf'])
    if uploaded_file:
        process_files(uploaded_file)
        st.success('File processed successfully.')
        with sq.connect('biomeddata.db') as connection:
            conn = connection.cursor()
            titles = conn.execute("SELECT DISTINCT title FROM reports").fetchall()
            for t in titles:
                st.write(t[0])
    #chat interface
if os.path.exists('./index_storage'):
    storage_context = StorageContext.from_defaults(persist_dir='./index_storage')
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()

    user_question = st.text_input('Ask a question about the reports/papers:')
    #user query handling
    if user_question:
        with st.chat_message('you'):
            st.write(user_question)
        with st.chat_message('assistant'):
            response = query_engine.query(user_question)
            st.write(response.response)
else: 
    st.info('No data found.')