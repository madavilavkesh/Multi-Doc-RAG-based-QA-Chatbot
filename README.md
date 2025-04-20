# Multi-Doc RAG-based Q&A Chatbot

## Project Description

A Retrieval-Augmented Generation (RAG) chatbot designed to answer questions from multiple uploaded documents (PDF, DOCX, URLs). The system utilizes LLaMA-4 via the Groq API to generate answers and processes documents using Sentence-Transformers for embeddings and FAISS for efficient similarity search. This allows the chatbot to provide relevant answers based on the content of the uploaded documents.

## Features
- Upload and query multiple document types (PDF, DOCX, URL).
- Generate accurate responses based on document embeddings and similarity search.
- Built using LLaMA-4 model via the Groq API for Q&A generation.
- Utilizes LangChain for conversation flow and document processing.
- Integrates Streamlit for the user interface.

## Tech Stack
- **Backend:** Python, LangChain, Sentence-Transformers, FAISS
- **Frontend:** Streamlit
- **APIs:** Groq API (for LLaMA-4), FAISS for document similarity search
- **Libraries:** Groq Python SDK, Sentence-Transformers, FAISS, LangChain

## Requirements

- Python 3.7+
- Streamlit
- LangChain
- FAISS
- Sentence-Transformers
- Groq Python SDK

You can install the dependencies by running:

```bash
pip install -r requirements.txt
```

## Setup and Usage

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Set up environment variables by creating a `.env` file in the root of the project with the following content:

```env
GROQ_API_KEY="your-groq-api-key-here"
USER_AGENT="YourChatbot/1.0"
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Access the chatbot UI on your browser.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
