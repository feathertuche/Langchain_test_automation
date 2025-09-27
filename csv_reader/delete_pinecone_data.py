from helper_functions import api_log
from pinecone_vector_connection.Pinecone_factory_connection import \
    ConnectorFactory


def clear_pinecone_index(index_type: str):
    try:
        connector = ConnectorFactory.get_connector(index_type)
        index, _ = connector.get_connection()

        api_log(msg=f"Deleting all vectors from index: {index_type}")
        (index.delete(delete_all=True))
        api_log(msg=f"Index '{index_type}' cleared successfully.")
        return True
    except Exception as e:
        api_log(msg=f"Error while clearing index '{index_type}': {str(e)}")
        return False


clear_pinecone_index("coverage")
clear_pinecone_index("testlog")
