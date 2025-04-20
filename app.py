import streamlit as st
from dotenv import load_dotenv
from utils.file_handlers import collect_inputs
from utils.embedding_utils import process_and_embed_documents
from utils.rag_pipeline import get_rag_chain
from utils.session_manager import initialize_session
import os

# Load API keys
load_dotenv()

# Streamlit UI setup
st.set_page_config(page_title="Multi-Doc RAG-based Chatbot", layout="wide")
st.title("📚🧠 Multi-Doc RAG-based Q&A Chatbot")

# Initialize session state
initialize_session()

# Sidebar: Inputs
with st.sidebar:
    st.header("Upload / Enter Input")

    # Collect inputs from user (URLs, PDFs, DOCX, and Text)
    user_inputs = collect_inputs()

    # Process documents and create vectorstore
    if st.button("🔍 Process Documents"):
        with st.spinner("Processing and embedding..."):
            vectorstore = process_and_embed_documents(user_inputs)
            st.session_state.vectorstore = vectorstore
            st.session_state.retriever = vectorstore.as_retriever()
            st.success("Documents processed successfully!")

# Main Chat Interface
if st.session_state.vectorstore:
    query = st.chat_input("Ask something about your documents...")

    if query:
        chain = get_rag_chain(st.session_state.retriever)
        result = chain({"question": query, "chat_history": st.session_state.chat_history})
        st.session_state.chat_history.append((query, result["answer"]))

    for q, a in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(q)
        with st.chat_message("assistant"):
            st.markdown(a)
