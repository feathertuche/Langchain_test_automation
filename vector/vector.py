import os
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class PineconeConn:
	def __init__(self):
		self.pine_index_name = os.getenv("PINECONE_INDEX_NAME")
		self.pine_embedding_model = os.getenv("EMBED_MODEL")
		self.index = None
		self.embedder = None


	@classmethod
	def get_pinecone_connection(cls):
		try:
			print("Pinecone connection initiating..")
			pine = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
			conn = cls()
			conn.index = pine.Index(host=os.getenv("PINECONE_HOST"))
			try:
			    conn.embedder = SentenceTransformer(conn.pine_embedding_model)
			except Exception as e:
				print(f"Failed to load embedding model: {embedding_model}")
				raise e
			print("Pinecone connection established..")
			return conn
		except ConnectionRefusedError as cre:
			print(f"Pinecone connection Failed with {str(cre)}")
		

def main():
	print(get_pinecone_connection())
 
if __name__ == '__main__':
	main()
