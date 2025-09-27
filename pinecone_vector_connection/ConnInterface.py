from abc import ABC, abstractmethod


class VectorStoreConnector(ABC):
    @abstractmethod
    def get_connection(self):
        pass
