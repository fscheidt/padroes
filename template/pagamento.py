from abc import ABC, abstractmethod
from typing import final

class Transacao():
    def __init__(self): ...


class Pagamento(ABC):
    def __init__(self):
        self.id = None
    
    def realizar_pagamento(self, valor):
        # 1. validação
        
        # 2. criar transação

        # 3. pagar

        # 4. gerar nota fiscal

        pass


class Pix(Pagamento):
    pass


# cliente
if __name__ == "__main__":
    pass