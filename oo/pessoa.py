from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome: str, renda: float):
        self.nome = nome
        self.renda = renda

    @abstractmethod
    def calculaIR(self) -> float:
        pass

class PessoaFisica(Pessoa):
    # sobrescreve o construtor da classe Pessoa pois PF 
    # fornece sua propria implementação
    def __init__(self, nome: str, renda: float, cpf: str):
        super().__init__(nome, renda) # chama o construtor de Pessoa
        self.cpf = cpf
    def calculaIR(self) -> float:
        return self.renda * 0.25

class PessoaJuridica(Pessoa):
    def __init__(self, nome: str, renda: float, cnpj: str):
        super().__init__(nome, renda) # chama o construtor de Pessoa
        self.cnpj = cnpj
    def calculaIR(self) -> float:
        return self.renda * 0.18

# pf = Pessoa("Maria", 80_000)
# print(pf.calculaIR())  # TypeError: Can't instantiate abstract class Pessoa

pf = PessoaFisica("Maria", 100_000, "100.999.000-99")
print(pf.calculaIR())
print(pf.cpf)

pj = PessoaJuridica("SUPER DIA", 20_000_000, "0001/19109910101")
print(pj.calculaIR())
print(pj.cnpj)
