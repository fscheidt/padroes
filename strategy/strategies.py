from abc import ABC, abstractmethod
import hashlib

class HashStrategy(ABC):
    """ Define a familia de algoritmos de hash do password """
    @abstractmethod
    def encrypt(self, password: str) -> str:
        pass

class Md5Strategy(HashStrategy):
    def encrypt(self, password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()

class Sha1Strategy(HashStrategy):
    def encrypt(self, password: str) -> str:
        return hashlib.sha1(password.encode()).hexdigest()
    
# ======================
def create(choice: int) -> HashStrategy:
    """ Factory (auxiliar na criacao de estrategias) """
    # TODO: tornar dinamico
    if choice == 1:
        return Md5Strategy()
    if choice == 2:
        return Sha1Strategy()
    raise ValueError("unknow strategy")


