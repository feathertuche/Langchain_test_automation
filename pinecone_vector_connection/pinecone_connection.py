import os
from dotenv import load_dotenv
from pinecone import Pinecone, PineconeException
# from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings
from helper_functions import api_log
from .ConnInterface import VectorStoreConnector

load_dotenv()


class PineconeConnector(VectorStoreConnector):
    def __init__(self, index_name: str, embed_model: str, host: str):
        self.index_name = index_name
        self.embed_model = embed_model
        self.host = host

    def get_connection(self):
        try:
            api_log(msg="******* This is a Pinecone connection file ******")
            api_log(msg=f"Connecting to Pinecone index: {self.index_name}")
            pine = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
            index = pine.Index(host=self.host)
            api_log(msg=f"Successfully connected to Pinecone index: {self.index_name}")
        except PineconeException as pe:
            api_log(msg=f"Pinecone connection failed: {str(pe)}")
            raise pe
        except Exception as e:
            api_log(msg=f"Unexpected error while connecting to Pinecone: {str(e)}")
            raise e

        try:
            #embedder = SentenceTransformer(self.embed_model)
            embedder = HuggingFaceEmbeddings(model_name=self.embed_model)
            api_log(msg=f"Embedding model '{self.embed_model}' loaded successfully.")
        except ValueError as ve:
            api_log(msg=f"Embedding model loading failed: {str(ve)}")
            raise ve
        except Exception as e:
            api_log(msg=f"Unexpected error while loading embedder: {str(e)}")
            raise e

        return index, embedder
