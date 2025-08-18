""" 
Fornece um ponto de acesso para a classe cliente
delegando a execucao do calculo do hash para a estrategia
concreta
"""
import strategies


class HashContext():
    def __init__(self, strategy: strategies.HashStrategy):
        self.strategy = strategy
    
    def hash(self, password: str) -> str:
        return self.strategy.encrypt(password)


def select_strategy() -> HashContext:
    """
    Helper function - read client strategy choice and returns a concrete Strategy
    """
    print("-"*40)
    print("Estrategias Hash disponiveis")
    print("-"*40)
    # TODO: melhorar (tornar dinamico)
    print("""
    1 - md5
    2 - sha1
    """)
    choice = int(input("Escolha a opção: "))
    strategy = strategies.create(choice)
    return HashContext(strategy)
