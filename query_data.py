# query_data.py

# Import necessary modules
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from dotenv import load_dotenv

# Load environment variables (in case the OpenAI API key is needed)
load_dotenv()

# Initialize Chroma client and collection
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("my_documents")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

# Set up storage context with the correct persist_dir
storage_context = StorageContext.from_defaults(
    vector_store=vector_store,
    persist_dir="./saved_index"  # Match the directory used during indexing
)

# Load the index from storage
index = load_index_from_storage(storage_context=storage_context)
print("Index loaded from disk.")

# Set up the query engine to start querying
query_engine = index.as_query_engine()

# Run a sample query
response = query_engine.query("What is the best way to price AI solutions?")
print("Query Result:", response)
