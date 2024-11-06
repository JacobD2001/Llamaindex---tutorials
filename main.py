# Step 1: Import necessary modules
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from dotenv import load_dotenv

load_dotenv()

# Step 2: Load documents as Document objects from the directory
documents = SimpleDirectoryReader('./data').load_data()
print("Loading documents done.")

# Step 3: Set up Chroma as the vector store
# Initialize Chroma client, which will save data to ./chroma_db folder
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("my_documents")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Step 4: Create the vector index with storage context and save it to disk
vector_index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, show_progress=True
)
print("Indexing complete.")

# Step 5: Persist the index for later use
vector_index.storage_context.persist(persist_dir="./saved_index")
print("Index persisted to disk.")

# Step 2: Load documents as Document objects from the directory
documents = SimpleDirectoryReader('./data').load_data()
print("Loading documents done.")

# Step 3: Set up Chroma as the vector store
# Initialize Chroma client, which will save data to ./chroma_db folder
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("my_documents")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Step 4: Create the vector index with storage context and save it to disk
vector_index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, show_progress=True
)
print("Indexing complete.")

# Step 5: Persist the index for later use
vector_index.storage_context.persist(persist_dir="./saved_index")
print("Index persisted to disk.")
