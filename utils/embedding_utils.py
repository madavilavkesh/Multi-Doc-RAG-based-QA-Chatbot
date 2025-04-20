import faiss
import numpy as np
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.document_loaders import WebBaseLoader
from langchain.docstore.document import Document
from utils.file_handlers import extract_text_from_pdf, extract_text_from_docx

def process_and_embed_documents(inputs):
    documents = []

    # Process URLs
    for link in inputs.get("Link", []):
        try:
            loader = WebBaseLoader(link)
            docs = loader.load()
            documents.extend(docs)
        except Exception as e:
            st.warning(f"❌ Error loading URL: {link} — {e}")

    # Process PDFs
    for pdf_file in inputs.get("PDF", []):
        try:
            text = extract_text_from_pdf(pdf_file)
            if text.strip():
                documents.append(Document(page_content=text))
        except Exception as e:
            st.warning(f"❌ Error processing PDF: {pdf_file.name} — {e}")

    # Process DOCX
    for docx_file in inputs.get("DOCX", []):
        try:
            text = extract_text_from_docx(docx_file)
            if text.strip():
                documents.append(Document(page_content=text))
        except Exception as e:
            st.warning(f"❌ Error processing DOCX: {docx_file.name} — {e}")

    # Custom Text
    for text_input in inputs.get("Text", []):
        if text_input.strip():
            documents.append(Document(page_content=text_input.strip()))

    if not documents:
        raise ValueError("❗ No valid input content found. Please upload or enter something.")

    # Combine and split text
    full_text = "\n".join([doc.page_content for doc in documents])
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(full_text)

    if not chunks:
        raise ValueError("❗ No chunks to embed. The provided content might be too short or empty.")

    # Load embedding model
    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    # Create FAISS index
    sample_vector = embed_model.embed_query("sample")
    index = faiss.IndexFlatL2(len(sample_vector))
    vectorstore = FAISS(
        embedding_function=embed_model.embed_query,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={}
    )

    # Add text chunks to vectorstore
    vectorstore.add_texts(chunks)

    return vectorstore
