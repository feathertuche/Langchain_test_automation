from langchain_pinecone import PineconeVectorStore

from pinecone_vector_connection.vector import PineconeConn


class PineconeSemanticSearch:
    def __init__(self, text_key: str):
        self.text_key = text_key
        self.index, self.embedder = PineconeConn.get_pinecone_connection()
        self.vector_store_search = PineconeVectorStore(
            index=self.index, embedding=self.embedder, text_key=self.text_key
        )

    def search_pinecone(self, query: str, k: int = 5):
        return self.vector_store_search.asimilarity_search(query=query, k=k)


semantic_search = PineconeSemanticSearch("page_content")
results = semantic_search.search_pinecone(
    query="Which modules lack test coverage?", k=5
)
