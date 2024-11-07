from abc import ABC, abstractmethod

class Observer(ABC): 
    """ Quem esta interessado em ser notificado """
    @abstractmethod
    def update(self): ...

class Subject(ABC):
    """ Aquele que notifica """
    @abstractmethod
    def subscribe(self, observer: Observer): ...
    @abstractmethod
    def cancel(self, observer: Observer): ...
    @abstractmethod
    def notify(self): ...

# Item fora do Estoque Nofitier (Listener)
class Estoque(Subject): 
    def __init__(self): 
        self.subscribers = [] # lista de inscritos
        self.items = []

    def subscribe(self, observer: Observer): 
        self.subscribers.append(observer)

    def cancel(self, observer: Observer):
        self.subscribers.remove(observer)
    
    def notify(self):
        """ eh o disparo da notificacao """
        print("> notificando inscritos")
        for sub in self.subscribers:
            sub.update()

    def new_item(self, item: str):
        """ ocorrencia do evento de chegada de um item """
        print(f"> {item} chegou no estoque")
        self.items.append(item)
        self.notify()

class Cliente(Observer):
    def __init__(self, nome):
        self.nome = nome
        self.subject = None
    def add_item(self, item, subject: Subject):
        """ inscricao para ser notificado sobre um produto """
        self.item = item
        self.subject = subject
        self.subject.subscribe(self)  # self eh a instancia de um cliente
    def update(self):
        """ o que o cliente vai fazer com a notificacao recebida """
        if self.item in self.subject.items:
            print(f"usuario {self.nome} notificado da chegada do item {self.item}")
            # encaminhar para o carrinho de compras ...
            # caso deseja nao ser mais notificado:
            self.subject.cancel(self)


if __name__ == "__main__":
    estoque = Estoque()  # sujeito
    maria = Cliente("Maria") # observador
    # maria se inscreve para receber informacoes sobre a chegada do item 
    maria.add_item("Phone A2", estoque)   

    joao = Cliente("Joao") # observador
    joao.add_item("Phone A4", estoque)

    estoque.new_item("Phone A2") # Evento gatilho da notificacao
    estoque.new_item("Phone A4") # 
    estoque.new_item("Phone A8") # ninguem inscrito
