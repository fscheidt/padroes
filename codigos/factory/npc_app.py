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
  # (3) inimigo ataca Player e atualizar HP
  inimigo.atacar(mario)
  # (4) exibir HP do player

"""
Atividade 1:
a) Implementar o método Ataque da Classe NPC
- Dragon, força de ataque=15
- Bowse, força ataque=10

b) Implementar o Factory da Classe Player:
- Mario, hp=100, defesa=8
- Joker, hp=120, defesa=5

c) Gerar 2 inimigos usando o NPCFactory, para atacar 1 player. Exibir o HP do player.

"""
