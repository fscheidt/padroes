# Objetivo: delegar ao Factory a criação
# de objetos do tipo NPC
# NPC - Non-player character.
from enum import Enum
class NPC:
  def atacar(): 
    pass

class Player:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp

class Dragon(NPC):
  def atacar(self):
    print("ataque do dragon")
    # diminuir HP do Player
    # print saude do Player

class Bowse(NPC):
  def atacar(self):
    print("ataque do bowse")

class NpcType(Enum):
  DRAGON=0
  BOWSE=1

class NpcFactory:
  @staticmethod
  def create(type: NpcType):
    if type == NpcType.DRAGON:
      return Dragon()
    return Bowse()

if __name__ == "__main__":
  # (1) pede ao factory uma instancia de inimigo
  # inimigo = NpcFactory.create(NpcType.DRAGON)
  inimigo = NpcFactory.create(NpcType.BOWSE)
  # (2) cria uma instancia de jogador:
  mario = Player("Mario", 100)
  
  inimigo.atacar(mario)
