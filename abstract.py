from abc import ABC
class Pagamento(ABC):  # classe abstrata
    def __init__(self, valor):  # metodo construtor
        # atributo, inicializado na criacao do objeto  
        self.valor = valor if valor > 0 else 0  
    def status(self):
        print(f"valor pagamento: {self.valor:.2f}")

class PagamentoPix(Pagamento): # Herda de Pagamento
    def __init__(self, valor):
        super().__init__(valor)  # super eh a classe Pagamento

class PagamentoCredito(Pagamento): # Herda de Pagamento
    def __init__(self, valor):
        super().__init__(valor) 
        self.valor = self.valor * 1.1  # adiciona acrescimo de 10%

if __name__ == "__main__":
    pag = PagamentoPix(100)
    pag.status()
    
    pag = PagamentoCredito(100)
    pag.status()

    pag = PagamentoPix(-100)
    pag.status()
    