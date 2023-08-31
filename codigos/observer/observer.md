# Exemplo python Observer
- Notificação de chegada de produtos no estoque

```python

"""
The Observer 👀

Permite que um objeto notifique outros objetos na 
ocorrência de determinado evento.

Essa funcionalidade permite que objetos se inscrevam a 
certos eventos.

Envolvidos:
- Subject: representa a entidade na qual os observadores estão interessados 
- Observer: representa todos os objetos que serao notificados quando o estado do Subject mudar

"""

from abc import ABC

class Subject(ABC):
    """ Abstract subject """
    def inscrever(self, observer):
        pass
    def sair(self, observer):
        pass
    def notificar(self):
        pass

class Observer(ABC):
    """ Abstract Observer """
    def atualizar(self):
        pass    


if __name__ == '__main__':
    print('Observer - Notificação de produtos')

```