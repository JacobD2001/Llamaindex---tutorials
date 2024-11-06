from llama_index.core import SimpleDirectoryReader

documnets = SimpleDirectoryReader('./data').load_data()

print("loading documents done.")

