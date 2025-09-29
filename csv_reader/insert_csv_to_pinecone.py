import uuid

from csv_reader.pinecone_csv_reader import read_test_csv_file
from helper_functions import api_log
from pinecone_vector_connection.Pinecone_factory_connection import \
    ConnectorFactory


def insert_data_pinecone(filename: str, index_type: str):
    api_log(msg="******CSV file Insertion in Pinecone through Langchain******")

    try:
        api_log(msg='1')
        connector = ConnectorFactory.get_connector(index_type)
        api_log(msg='2')
        index, embedder = connector.get_connection()
        api_log(msg='3')
    except Exception as e:
        api_log(msg='4')
        api_log(msg=f"There was an exception while connecting to Pinecone: {str(e)}")
        return 0

    try:
        api_log(msg='5')
        documents = read_test_csv_file(filename)
        api_log(msg='6')
        api_log(msg="...FETCHING metadata from CSV file...")
        for i, doc in enumerate(documents):
            api_log(msg='7')
            vector = embedder.encode(doc.page_content)
            api_log(msg='8')
            metadata = doc.metadata.copy()
            api_log(msg='9')
            metadata["page_content"] = doc.page_content
            api_log(msg=f'THIS IS A METADATA: {metadata}')
            api_log(msg='10')
            index.upsert([
                {
                    "id": str(uuid.uuid4()),
                    "values": vector.tolist(),
                    "metadata": metadata,
                }
            ])
            api_log(msg='11')
            api_log(msg=f"Inserted doc-{i}")

        api_log(msg="All documents inserted successfully.")
        return 1
    except Exception as e:
        api_log(msg=f"There was an exception during insertion: {str(e)}")
        return 0


insert_data_pinecone("coverage_report.csv", "coverage")
insert_data_pinecone("test_logs.csv", "testlog")
