from enum import Enum
from fachada import ReservaFacade
""" 
PADRÃO DE PROJETO FACTORY 
    - fábrica de usuários
"""
class UserAbstract:
    def __init__(self, id):
        self.id = id
    def login(self):
        print("user login...")
class Admin(UserAbstract):
    def login(self):
        print("admin login...")
class User(UserAbstract):
    ...
class Visitor(UserAbstract):
    ...
class UserType(Enum):  # tipo Enum
    admin = "admin"
    user = "user"
    visitor = "visitor"
class UserFactory:  # Fabrica de usuarios
    @staticmethod
    def create(type: str) -> UserAbstract:
        fachada = ReservaFacade()
        fachada.reserva_pacote()
        if type == UserType.admin.value:
            return Admin(100)
        elif type == UserType.user.value:
            return User(50)
        elif type == UserType.visitor.value:
            return Visitor(1)
        else:
            raise Exception(f"unknow user type: {type}")

if __name__ == "__main__":
    admin = UserFactory.create(UserType.admin.value)  # admin = Admin()
    admin.login()
    maria = UserFactory.create(UserType.user.value)
    maria.login()
    # u = UserFactory.create("normal") # nao existe logo lança exception
    # u.login()
