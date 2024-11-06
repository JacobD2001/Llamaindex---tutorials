# app.py

import streamlit as st
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from dotenv import load_dotenv

# Load environment variables (if needed)
load_dotenv()

# Initialize Chroma client and collection (same as query code)
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("my_documents")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

# Set up storage context with the correct persist_dir
storage_context = StorageContext.from_defaults(
    vector_store=vector_store,
    persist_dir="./saved_index"  # Ensure this matches the indexing persist_dir
)

# Load the index from storage
index = load_index_from_storage(storage_context=storage_context)
query_engine = index.as_query_engine()

# Streamlit UI for Chat Interface
st.title("💬 AAA Foundations helper")
st.write("Ask questions about the foundations module.")

# Session state for storing the chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat Input Section
with st.form("chat_form", clear_on_submit=True):
    user_query = st.text_input("Type your query here:")
    submit_button = st.form_submit_button("Send")

# Process the user query
if submit_button and user_query:
    # Add the user query to the chat history
    st.session_state.chat_history.append(("User", user_query))

    # Get response from the query engine
    response = query_engine.query(user_query)
    
    # Append response to the chat history
    st.session_state.chat_history.append(("Bot", response.response))  # Use `.response` to get text

# Display the conversation in chat format
for sender, message in st.session_state.chat_history:
    if sender == "User":
        st.markdown(f"**🧑 You:** {message}")
    else:
        # Display bot's response with expander for full response
        with st.expander("🤖 Bot's Response"):
            st.write(message)  # Display full response in a readable format
