import os
#load api key
from dotenv import load_dotenv
load_dotenv()
from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
def indexengine():
    docs = SimpleDirectoryReader("./biodata").load_data()
    return VectorStoreIndex.from_documents(docs)
