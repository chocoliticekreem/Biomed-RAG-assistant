import os
#load api key
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
st.title("Biomed Research Assistant")

#create cache 
from indexengine import indexengine
if "index" not in st.session_state:
    st.session_state.index = indexengine()

#input
query = st.text_input("Ask a question about the report:")

#output
if query:
    query_engine = st.session_state.index.as_query_engine()
    response = query_engine.query(query)
    st.write(response)