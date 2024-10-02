from abc import ABC
class Pagamento(ABC):
    ...
    
class PagamentoPix(Pagamento):
    ...

if __name__ == "__main__":
    pag = Pagamento()

