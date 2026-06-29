import pypdf2
import chromadb
import uuid

chroma_client = chromadb.PersistentClient(path = "./chromdadb")
collection = chroma_client.get_or_create_collection(name="test_collection")