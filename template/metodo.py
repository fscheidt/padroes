# METODO TEMPLATE  
from abc import ABC, abstractmethod
from typing import final
class Pagamento(ABC):
    def create_transaction(self):
        return 1001
    
    @abstractmethod
    def pagar(self): ...

    def gerar_nota(self):
        print("3. nota fiscal gerada para transacao=id")

    @final # nao pode ser sobrescrito
    def realizar_pagamento(self):
        # Passos do método template
        # 1. criar id transação <- concreto
        id = self.create_transaction()
        print(f"1. Transacao {id} gerada")
        # 2. pagar <- abstrato
        self.pagar()

        # 3. gerar nota fiscal
        self.gerar_nota()
        print("="*40)

class Pix(Pagamento):
    def pagar(self):
        print("Pagamento pix")

class Cartao(Pagamento):
    def pagar(self):
        print("Pagamento Cartao")

# cliente
if __name__ == "__main__":
    pgto = Pix()
    pgto.realizar_pagamento()

    pgto = Cartao()
    pgto.realizar_pagamento()
