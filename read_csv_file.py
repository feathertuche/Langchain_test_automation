import os
from vector.vector import PineconeConn
from langchain_community.document_loaders import CSVLoader
from langchain_pinecone import PineconeVectorStore
from helper_functions import api_log


def read_test_csv_file(filename):
	api_log(msg="***************READ CSV FILE BLOC*****************")
	if not filename.lower().endswith('.csv'):
		raise ValueError(f"'Invalid file format: {filename}, please check the file name and try again..'")
	api_log(msg=f"Reading and fetching data from  CSV file: {filename}, please wait a while...")
	lang_csv_data = CSVLoader(file_path=filename,
					autodetect_encoding=True,
					csv_args = {
						'delimiter': ',',
    						'quotechar': '"',
    						'fieldnames': ['Index', 'Height', 'Weight']
					}
	)
	docs = lang_csv_data.load()
	return docs
	


def insert_data_pinecone(filename):
	import uuid
	api_log(msg="******CSV file Insertion in Pinecone through Langchain******")
	try:
		pine_conn = PineconeConn().get_pinecone_connection()
	except Exception as e:
		api_log(msg=f"There was an exception while connecting to Pinecone: {str(e)}")
	
	try:
		get_csv_data =  read_test_csv_file(filename)
		
		api_log(msg="...FETCHING metadata from CSV file...")
		for i, documents in enumerate(get_csv_data):
			vector = pine_conn.embedder.encode(documents.page_content)
			pine_conn.index.upsert([
				{
				    "id": str(uuid.uuid4()),
				    "values": vector.tolist(),
				    "metadata": documents.metadata
				}
			    ])
			api_log(msg=f"Inserted doc-{i}")
		api_log(msg=f"All Document Inserted successfully...")
		return 1
	except Exception as e:
		api_log(msg=f"there is an exception: {str(e)}")
		
print(insert_data_pinecone('test_logs.csv'))
