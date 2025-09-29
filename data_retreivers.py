from langchain_pinecone import PineconeVectorStore
from pinecone_vector_connection.Pinecone_factory_connection import ConnectorFactory
from helper_functions import api_log


class PineconeSemanticSearch:
    def __init__(self, text_key: str):
        self.text_key = text_key

    def search_pinecone(self, query: str, k: int = 5):
        api_log(msg="******* This is a Semantic search bloc *******")
        result = []
        for index_type in ["coverage", "testlog"]:
            try:
                connector = ConnectorFactory.get_connector(index_type)  # returns PineconeConnector
                index, embedder = connector.get_connection()

                vector_store_search = PineconeVectorStore(
                    index=index, embedding=embedder, text_key=self.text_key
                )
                semantic_test_search = vector_store_search.similarity_search(query=query, k=k)
                result.extend(semantic_test_search)

            except Exception as e:
                api_log(msg=f"Error during semantic search on index '{index_type}': {str(e)}")

        return result


semantic_search = PineconeSemanticSearch("page_content")
results = semantic_search.search_pinecone(
    query="Which modules lack test coverage?", k=5
)
