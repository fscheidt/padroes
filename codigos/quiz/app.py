import json

# classe Model
class Pais:
  def __init__(self, nome, continente):
    self.nome = nome
    self.continente = continente
  def __repr__(self) -> str:
    return f"<Pais> Nome: {self.nome} - ${self.continente}"

# PaisFactory

class LoadData:
  """ classe Utilitaria carregar o JSON
  le dados do arquivo json e retorna um dicionario """
  @staticmethod
  def getJson(filename):
    with open(filename,"r") as f:
      return json.load(f)

if __name__ == "__main__":
  # data representa o dicionario
  data = LoadData.getJson("quiz.json")
  # print(data)
  paises = data['paises']
  # print(paises)
  for p in paises:
    pais = Pais(p['nome'], p['continente'])
    if pais.continente == "America":
      print(pais)
