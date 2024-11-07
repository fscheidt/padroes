from abc import ABC, abstractmethod
class Pagamento(ABC):  
    """ Interface da Estrategia de Pagamento """
    def __init__(self, valor):
        self.valor = valor if valor > 0 else 0  
    def status(self):
        print(f"valor pagamento: {self.valor:.2f}")
    @abstractmethod
    def realizar(self):
        ...

class PagamentoPix(Pagamento): # Herda de Pagamento
    def __init__(self, valor):
        super().__init__(valor)  # super eh a classe Pagamento
    def realizar(self):
        print("pagamento pix")

class PagamentoCredito(Pagamento): # Herda de Pagamento
    def __init__(self, valor):
        super().__init__(valor) 
        self.valor = self.valor * 1.1  # adiciona acrescimo de 10%
    def realizar(self):
        print("pagamento credito")

class AppPag:
    """ Contexto - Aplicação onde se seleciona a estratégia """
    def __init__(self, strategy: Pagamento):
        """ inicializa a estrategia de pagamento """
        self.strategy = strategy
    def realizar_pagamento(self):
        self.strategy.realizar()
        ...

if __name__ == "__main__":
    pag = AppPag(PagamentoPix(100))
    pag.realizar_pagamento()
   
    pg_select = PagamentoCredito(100)
    pg_select.status()
    pag = AppPag(pg_select)
    pag.realizar_pagamento()
    