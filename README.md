# Biomed Intelligence Platform
**An integrated RAG and SQL engine for multi-modal biomedical data analysis.**

## Project Overview
This platform bridges the gap between unstructured documents (Lab Reports, PDFs) and structured databases (Experimental Results, SQL). Using a dual architecture, the system automatically extracts insights from PDFs, indexes them for semantic search, and catalogs metadata into a relational database.

## Core Features
- **Hybrid Data Ingestion:** Automated ETL pipeline that processes PDFs into both a Vector Store (LlamaIndex) and a Relational Database (SQLite).
- **Semantic Research Chat:** RAG-powered interface for natural language querying across multiple research documents.
- **Quantitative Analytics:** Integrated SQL viewer to track and manage cataloged reports.
- **Incremental Indexing:** Smart storage management that appends new data without re-processing historical records.
- **State Management:** Optimized Streamlit session handling for high-performance user interactions.

## Technical Stack
- **Languages:** Python, SQL
- **AI Framework:** LlamaIndex (VectorStore, StorageContext)
- **Database:** SQLite3
- **Frontend:** Streamlit 
- **PDF Parsing:** pdfplumber

## System Architecture
The project follows a **Modular Backend-Frontend** split:
1. `database.py`:  Handles text extraction, SQL insertion, and vector indexing logic.
2. `app.py`: Manages the UI/UX, file uploads, and session-based state.



## Installation & Setup
1. **Clone the Repo:**
  ```bash
  git clone [https://github.com/your-username/biomed-hybrid-intelligence.git](https://github.com/your-username/biomed-hybrid-intelligence.git)
  ```
   
2. **Install dependencies**
  ```bash 
  pip install -r requirements.txt
  ```

3. **Configure environment:** Create a .env file to store API key
  ```plaintext
  OPENAI_API_KEY=your_key_here
  ```

4. **Launch app**
  ```bash
  streamlit run app.py
  ```


