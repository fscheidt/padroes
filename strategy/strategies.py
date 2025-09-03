from abc import ABC, abstractmethod
import hashlib

class HashStrategy(ABC):
    """
    [1] STRATEGY 
    Define a familia de algoritmos de hash do password 
    """
    @abstractmethod
    def encrypt(self, password: str) -> str:
        pass

class Md5Strategy(HashStrategy):
    def encrypt(self, password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()

class Sha1Strategy(HashStrategy):
    def encrypt(self, password: str) -> str:
        return hashlib.sha1(password.encode()).hexdigest()

# Dicionário para expor as estratégias disponíveis
HASH_TYPES = {
    "md5": Md5Strategy,
    "sha1": Sha1Strategy,
    # "sha256": Sha256Strategy,
}

# ======================================
# Essa factory não faz parte do padrão Strategy
# Seu propósito é apenas facilitar a instanciação 
# das estratégias
def create(name: str, **kwargs) -> HashStrategy:
    """
    Factory de estrategias. 
        Uso: create("sha1")
    """
    try:
        cls = HASH_TYPES[name.lower()]
        return cls(**kwargs)
    except KeyError:
        raise ValueError(f"unknown hash strategy: {name!r}") from None
