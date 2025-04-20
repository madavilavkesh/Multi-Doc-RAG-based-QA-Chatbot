import streamlit as st
from docx import Document
from PyPDF2 import PdfReader
from langchain_community.document_loaders import WebBaseLoader
import uuid

# Extracts all text from a PDF file
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "\n".join([page.extract_text() for page in reader.pages])

# Extracts all text from a DOCX (Word) file
def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# Collects all user inputs (URLs, PDFs, DOCX files, custom text)
def collect_inputs():
    # Initialize dictionary to store inputs by type
    inputs = {"Link": [], "PDF": [], "DOCX": [], "Text": []}

    # Input field for comma-separated URLs (max 4) with a fixed key
    links = st.text_area("Enter up to 4 Website URLs (comma-separated)", key="link_input")
    if links:
        # Strip whitespace and keep only first 4 URLs
        inputs["Link"].extend([url.strip() for url in links.split(",")][:4])

    # Upload multiple PDF files (max 4) with a fixed key
    uploaded_pdfs = st.file_uploader("Upload up to 4 PDFs", type=["pdf"], accept_multiple_files=True, key="pdf_input")
    if uploaded_pdfs:
        inputs["PDF"].extend(uploaded_pdfs[:4])

    # Upload multiple DOCX files (max 4) with a fixed key
    uploaded_docx = st.file_uploader("Upload up to 4 DOCX files", type=["docx"], accept_multiple_files=True, key="docx_input")
    if uploaded_docx:
        inputs["DOCX"].extend(uploaded_docx[:4])

    # Optional text input from the user with a fixed key
    user_text = st.text_area("Add custom text (optional)", key="text_input")
    if user_text:
        inputs["Text"].append(user_text)

    return inputs
