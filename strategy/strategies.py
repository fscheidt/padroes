import hashlib
from abc import ABC, abstractmethod
class PasswordStrategy(ABC):
    """ Define a interface da estrategia da familia de algoritmos (hash) """
    @abstractmethod
    def encrypt(self, password: str) -> str:
        pass

class MD5Strategy(PasswordStrategy):
    def encrypt(self, password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()

class SHA1Strategy(PasswordStrategy):
    def encrypt(self, password: str) -> str:
        return hashlib.sha1(password.encode()).hexdigest()

def create(choice: int) -> PasswordStrategy:
    """ Factory de estrategias """
    if choice == 1: 
        strategy = MD5Strategy()
    elif choice == 2:
        strategy = SHA1Strategy()
    else:
        raise ValueError("invalid choice")
    return strategy
