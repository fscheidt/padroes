""" 
Fornece um ponto de acesso para a classe cliente
delegando a execucao do calculo do hash para a estrategia
concreta
"""
import strategies

def select_strategy() -> strategies.HashStrategy:
    """
    Helper function - read client strategy choice and returns a concrete Strategy
    """
    print("-"*40)
    print("Estrategias Hash disponiveis")
    print("-"*40)
    print("""
    1 - md5
    2 - sha1
    """)
    choice = int(input("Escolha a opção: "))
    return strategies.create(choice)

class HashContext():
    pass
