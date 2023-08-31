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

class Subject(ABC): # Aquele que notifica os interessados
    """ Abstract subject """
    def inscrever(self, observer):
        pass
    def sair(self, observer):
        pass
    def notificar(self):
        pass

class Observer(ABC): 
    # Clientes que inscrevem-se para receber notificacao
    """ Abstract Observer """
    def atualizar(self):
        pass    

# CLASSES CONCRETAS 
# 1. Notificador (Sujeito)
class Estoque(Subject):
    def __init__(self):
        self.produtos = []
        self.inscritos = [] # lista de observadores

    def inscrever(self, observer):
        if observer not in self.inscritos:
          self.inscritos.append(observer)
    
    def sair(self, observer):
        # remove da lista de inscritos determinado interessado
        if observer in self.inscritos:
          self.inscritos.remove(observer)
    
    def notificar(self):
        # executado quando determinado evento ocorrer
        # evento: chegada de um produto
        for observer in self.inscritos:
            # notificar os interessados
            observer.atualizar()

    def produto_recebido(self, produto):
        """ Evento gatilho da App - novo produto recebido  """
        print("="*40)
        print(f"[Evento] Produto recebido: {produto}")
        # atualizar estoque com o novo produto
        self.produtos.append(produto)
        # notificar interessados
        self.notificar()

# 2. Usuarios
class Usuario(Observer):
    def __init__(self, nome, produto=None, subject=None ):
        self.nome = nome
        self.produto = produto # Fone ouvido
        self.subject = subject
        if subject:
          subject.inscrever(self) # representa o proprio usuario

    def atualizar(self):
        if self.produto in self.subject.produtos:
            print(f"Notificando {self.nome}, produto {self.produto} disponivel")
            # opcional: usuario pode se desinscrever se desejar
            self.subject.sair(self)

if __name__ == '__main__':
    print('Observer - Notificação de produtos')
    estoque = Estoque()
    joao = Usuario("João", produto="Fone", subject=estoque)
    maria = Usuario("Maria", produto="Teclado", subject=estoque)

    # evento que dispara a notificação
    estoque.produto_recebido("Fone")
    # primeira entrega de teclado, notifica maria
    estoque.produto_recebido("Teclado")
    # segunda entrega, não notifica ninguem (não há inscritos)
    estoque.produto_recebido("Teclado")

