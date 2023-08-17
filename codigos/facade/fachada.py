# Fachada que liga um computador, e abstrai seus
# componentes atraves do metodo ligar() 
# 1 - PlacaMae
# 2 - CPU
# 3 - Memoria
# 4 - SSD
# 5 - Video
class PlacaMae:
  def __init__(self, boot):
    self.boot = boot
  def ligar(self):
    print("placa mae ligada")

class CPU:
  def __init__(self, profile):
    self.profile = profile
  def ligar(self):
    print("cpu inicializada")

class Memoria:
  def __init__(self, test):
    self.test = test
  def inicializar(self):
    print("memoria ok")

# Fachada - interface que liga o computador
class FachadaComputador:
  def __init__(self):
    self.placa = PlacaMae("bootNormal")
    self.cpu = CPU(profile="performance")
    self.mem = Memoria(test=True)

  def ligar(self):
    self.placa.ligar()
    self.cpu.ligar()
    self.mem.inicializar()

## uma parte do código - web, service, app ... 
# simular um cliente
if __name__ == "__main__":
  # deseja ligar o computador
  computador = FachadaComputador()
  computador.ligar()

