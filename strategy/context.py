""" 
Fornece um ponto de acesso para a classe cliente
delegando a execucao do calculo do hash para a estrategia
concreta
"""
from strategies import PasswordStrategy
class HashContext():
    def __init__(self, strategy: PasswordStrategy):
        self.strategy = strategy

    def hash(self, password: str) -> str:
        """ Ponto de acesso ao cliente """
        return self.strategy.encrypt(password)
    