from abc import ABC, abstractmethod
from enum import Enum
class TipoPessoa(str, Enum):
    PF = "PF"
    PJ = "PJ"

class Pessoa(ABC):
    def __init__(self, nome: str = None, renda: float = 0):
        self.nome = nome
        self.renda = renda

    @abstractmethod
    def calculaIR(self) -> float:
        pass

class PessoaFisica(Pessoa):
    def calculaIR(self) -> float:
        print("implementar")

class PessoaJuridica(Pessoa):
     def calculaIR(self) -> float:
        print("implementar")

