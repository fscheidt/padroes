from abc import ABC, abstractmethod
import hashlib

class HashStrategy(ABC):
    @abstractmethod
    def encrypt(self, password: str) -> str:
        pass
