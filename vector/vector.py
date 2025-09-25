import os
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class PineconeConn:
    def __init__(self, pine_index_name: str, pine_embedding_model: str):
        self.pine_index_name = pine_index_name
        self.pine_embedding_model = pine_embedding_model
        self.index = None
        self.embedder = None


@classmethod
def get_pinecone_connection(cls):
	try:
	    print("This is Pinecone connection block")
	    pine = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
	    print("Pinecone connection initiated")

	    index_name = os.getenv("PINECONE_INDEX_NAME")
	    embedding_model = os.getenv("EMBED_MODEL")

	    conn = cls(index_name, embedding_model)
	    conn.index = pine.Index(host=os.getenv("PINECONE_HOST"))
	    try:
		conn.embedder = SentenceTransformer(embedding_model)
	    except Exception as e:
		print(f"Failed to load embedding model: {embedding_model}")
		raise e
	except ConnectionRefusedError as cre:
		print(f"Pinecone connection Failed with {str(cre)}")
    return conn
    
 def main():
 	print(get_pinecone_connection())
 
 if __name__ == '__main__':
	main()
