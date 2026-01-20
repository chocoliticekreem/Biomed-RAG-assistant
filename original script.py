#enable file reading and vector indexing for semantic search
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
import os
API_KEY = os.getenv('API_KEY')

#Read input papers
docs = SimpleDirectoryReader("./biodata").load_data()
# Create the vector index
index = VectorStoreIndex.from_documents(docs)
# Chat engine
query_engine = index.as_query_engine()

#loop for user queries; break on 'exit'
while True:
    user_input = input("Ask a question about this report (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    response = query_engine.query(user_input)
    print(response)