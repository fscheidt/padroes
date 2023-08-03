class Pessoa:
  def __init__(self):
    print('init pessoa')
    self.nome = ""


class PessoaJuridica(Pessoa):
  # construtor com inicialização de valores default caso não seja definido
  def __init__(self, 
               nome, 
               cnpj, 
               email=None,
               renda=0,
               ):
    self.nome = nome
    self.email = email or "not found"
    self.cnpj = cnpj

if __name__ == "__main__":
  p1 = PessoaJuridica("Marcos","9292","email@a1.org")
  p2 = PessoaJuridica("Maria","111")
  print(p1.email)
  print(p2.email)

