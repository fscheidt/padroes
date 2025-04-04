import hashlib
from abc import ABC, abstractmethod
class PasswordStrategy(ABC):
    """ 1 - Interface da estrategia """
    @abstractmethod
    def encrypt(self, password: str) -> str:
        pass

class MD5Strategy(PasswordStrategy):
    def encrypt(self, password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()

class SHA1Strategy(PasswordStrategy):
    def encrypt(self, password: str) -> str:
        return hashlib.sha1(password.encode()).hexdigest()

def create() -> PasswordStrategy:
    """ TODO: Factory de estrategias """
    pass
