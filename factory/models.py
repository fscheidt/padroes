from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome: str = None, renda: float = 0):
        self.nome = nome
        self.renda = renda

    def calculaIR(self) -> float:
        pass

class PessoaFisica(Pessoa):
    pass

class PessoaJuridica(Pessoa):
    pass

