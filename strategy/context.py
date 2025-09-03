""" 
[2] CONTEXTO

Fornece um ponto de acesso para o cliente
delegando a execucao do calculo do hash para a estrategia
concreta

"""
import strategies


class HashContext():
    """ 
    Contexto
    """
    def __init__(self, strategy: strategies.HashStrategy):
        self.strategy = strategy
    
    def hash(self, password: str) -> str:
        return self.strategy.encrypt(password)


def select_strategy() -> HashContext:
    """
    Helper function - simulação da UI onde o cliente seleciona no menu um algoritmo hash
    e retorna o contexto, que permite executar a função hash 
    """
    print("-"*40)
    print("Estrategias Hash disponiveis")
    print("-"*40)

    options = {i: name for i, name in enumerate(
        sorted(strategies.HASH_TYPES.keys()), start=1
    )}
    for i, name in options.items():
        print(f"{i} - {name}")

    while True:
        try:
            choice = int(input("Escolha a opção: "))
            name = options[choice]
            strat = strategies.create(name)
            return HashContext(strat)
        except (ValueError, KeyError):
            print("Invalid choice")
