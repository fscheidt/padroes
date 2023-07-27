from abc import ABC
class Pessoa(ABC): # pessoa eh definido como abstrata
  def __init__(self): # construtor da classe
    print('init pessoa')
    self.nome = "" # eh o this (java)

class PessoaFisica(Pessoa):
  def __init__(self):
    super().__init__() # chama o construtor da classe Pessoa
    self.cpf = ""
    self.__id = 1000 # "__" convencao de atributo private

  def printDados(self):
    print(self.nome + " - cpf: " + self.cpf)

  @staticmethod
  def printOla():
    print("ola sou uma PF")

class PessoaJuridica(Pessoa):
  def __init__(self):
    self.cnpj = ""

if __name__ == "__main__":
  maria = PessoaFisica()
  maria.nome = "Maria"
  maria.cpf = "10101010101"
  maria.printDados()
  print(id(maria))
  joao = PessoaFisica()
  joao.nome = "Joao"
  # joao.setNome("joao")
  joao.cpf = "999919191"
  joao.printDados()
  print(id(joao))

  PessoaFisica.printOla()

