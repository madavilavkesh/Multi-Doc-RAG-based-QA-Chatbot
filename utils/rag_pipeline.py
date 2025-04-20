import os
from langchain.chains import ConversationalRetrievalChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables (e.g., API keys)
load_dotenv()
groq_token = os.getenv("GROQ_API_KEY")  # Fetch Groq API key securely

# Create and return the RAG chain using LLM + document retriever
def get_rag_chain(retriever):
    # Initialize Groq LLM with desired model and parameters
    llm = ChatGroq(
        temperature=0.6,
        groq_api_key=groq_token,
        model_name="meta-llama/llama-4-scout-17b-16e-instruct"
    )

    # Build the conversational RAG chain (chat + memory)
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=False  # Set True if you want to show sources
    )
