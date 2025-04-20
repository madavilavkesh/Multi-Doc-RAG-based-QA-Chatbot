import streamlit as st

# Initialize session state variables (only if not already created)
def initialize_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []  # Stores (question, answer) pairs
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None  # Will hold FAISS vector index
    if "retriever" not in st.session_state:
        st.session_state.retriever = None  # Stores retriever linked to vectorstore



