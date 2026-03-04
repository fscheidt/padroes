from abc import ABC, abstractmethod
from typing import final

class Transacao():
    def __init__(self):
        import uuid
        self.id = uuid.uuid4()

class Pagamento(ABC):
    def __init__(self):
        self.id = None
        self.valor = None
    
    # 1 - etapa concreta
    def validate(self, valor):
        assert valor > 0
        self.valor = valor
        return
    
    # 2 - etapa concreta
    def create_transaction(self):
        self.id = Transacao().id

    # 3 - etapa Abstrata
    @abstractmethod
    def pagar(self): ...

    # 4 - concreto 
    def gerar_nota(self):
        print(f"4 - Nota {self.id} gerada")
    
    @final
    def realizar_pagamento(self, valor):
        """ Método template """
        # 1. validação
        print("1 - validação de valores, descontos, parcelas, ...")
        self.validate(valor)

        # 2. criar transação
        self.create_transaction()
        print("2 - ID da transação gerado")

        # 3. pagar (conforme forma de pagamento escolhida)
        self.pagar()

        # 4. gerar nota fiscal
        self.gerar_nota()

class Pix(Pagamento):
    def pagar(self):
        print(f"3 - pagamento {self.valor} realizado (pix)")

class Bitcoin(Pagamento):
    def pagar(self):
        self.valor = self.valor * 0.9
        print(f"3 - pagamento de {self.valor} realizado (Bitcoin)")
    def gerar_nota(self):
        print("4 - não necessário")


# cliente
if __name__ == "__main__":
    pgto = Pix()
    pgto.realizar_pagamento(1000)
    print("="*40)
    pgto = Bitcoin()
    pgto.realizar_pagamento(1000) # desconto de 10%

