import os
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from helper_functions import api_log

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
			api_log(msg="Pinecone connection initiating..")
			pine = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
			conn = cls()
			conn.index = pine.Index(host=os.getenv("PINECONE_HOST"))
			try:
			    conn.embedder = SentenceTransformer(conn.pine_embedding_model)
			except Exception as e:
				api_log(msg=f"Failed to load embedding model: {conn.embedder} with {str(e)}")
				raise e
			api_log(msg="Pinecone connection established..")
			return conn
		except ConnectionRefusedError as cre:
			api_log(msg=f"Pinecone connection Failed with {str(cre)}")
		

def main():
	get_pinecone_connection()
 
if __name__ == '__main__':
	main()
