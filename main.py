from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.ingestion import IngestionPipeline

documents = SimpleDirectoryReader('./data').load_data()

print("loading documents done.")

# Set up the text splitter transformation
text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=10)

# Set up the ingestion pipeline with the splitter
pipeline = IngestionPipeline(transformations=[text_splitter])

# Run the pipeline to split the documents
nodes = pipeline.run(documents=documents)
print("Document splitting done.")