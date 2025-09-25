import os
from vector.vector import PineconeConn
from langchain_community.document_loaders import CSVLoader
from langchain_pinecone import PineconeVectorStore

'''
def read_test_csv_file(filename):
	lang_csv_data = CSVLoader(file_path=filename,
					autodetect_encoding=True,
					csv_args = {
						'delimiter': ',',
    						'quotechar': '"',
    						'fieldnames': ['Index', 'Height', 'Weight']
					}
	)
	docs = lang_csv_data.load()
	#print(" ")
	#print('DOC-0', docs[0])
	#print('[THIS IS METADATA] ::',docs[0].metadata)
	return docs
	
print(read_test_csv_file('test_logs.csv'))
'''
def insert_data_pinecone():
	print("This function connects to Pinecone through Langchain...")
	try:
		pine_conn = PineconeConn().get_pinecone_connection()
	except Exception as e:
		print(f"There was an exception while connecting to Pinecone with {str(e)}")
		
print(insert_data_pinecone())
