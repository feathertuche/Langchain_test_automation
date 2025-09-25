import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# load environment variables from env file
load_dotenv()

# Create Pinecone client
pine = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    host=os.getenv("PINECONE_HOST")
)
print(pine.list_indexes())