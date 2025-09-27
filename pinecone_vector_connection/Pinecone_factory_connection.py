import os

from pinecone import PineconeException

from helper_functions import api_log
from pinecone_vector_connection.ConnInterface import VectorStoreConnector
from pinecone_vector_connection.pinecone_connection import PineconeConnector


class ConnectorFactory:
    @staticmethod
    def get_connector(index_type: str) -> VectorStoreConnector:
        api_log(msg="****** This is a Factory Function ******")
        try:
            embed_model = os.getenv("EMBED_MODEL")

            if index_type == "coverage":
                index_name = os.getenv("PINECONE_COVERAGE_INDEX")
                host = os.getenv("PINECONE_COVERAGE_HOST")
            elif index_type == "testlog":
                index_name = os.getenv("PINECONE_TESTLOG_INDEX")
                host = os.getenv("PINECONE_TESTLOG_HOST")
            else:
                raise ValueError(f"Unknown index type: {index_type}")

            api_log(msg=f"Creating connector for index: {index_name}")
            return PineconeConnector(
                index_name=index_name, embed_model=embed_model, host=host
            )

        except PineconeException as pe:
            api_log(msg=f"Pinecone-specific error while creating connector: {str(pe)}")
            raise pe
        except Exception as e:
            api_log(msg=f"Unexpected error in ConnectorFactory: {str(e)}")
            raise e


if __name__ == "__main__":
    server = ConnectorFactory
    server.get_connector("index_type")
