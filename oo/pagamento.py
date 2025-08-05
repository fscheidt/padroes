from abc import ABC, abstractmethod

class Pagamento(ABC): ...

class PagamentoPix(Pagamento): ...

class PagamentoBoleto(Pagamento): ...

class PagamentoCartao(Pagamento): ...

# ====== TEMPO DE EXECUÇÃO =======
if __name__ == "__main__":
    valor = 100
    # usuário "escolhe" a forma de pagamento
    # exibe o valor final
    ...
    