""" 
Fornece um ponto de acesso para a classe cliente
delegando a execucao do calculo do hash para a estrategia
concreta
"""
import strategies

def select_strategy() -> strategies.PasswordStrategy:
    """    Helper function - read user choice    """
    print("-"*40)
    print("Algoritmos Hash disponiveis")
    print("-"*40)
    print("""
    1 - md5
    2 - sha1
    """)
    choice = int(input("Escolha a opção: "))
    return strategies.create(choice)

class HashContext():
    def __init__(self, strategy: strategies.PasswordStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: strategies.PasswordStrategy):
        self.strategy = strategy

    def hash(self, password: str) -> str:
        """ Ponto de acesso ao cliente """
        return self.strategy.encrypt(password)
    
    