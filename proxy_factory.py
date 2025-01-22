class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name

    def set_id(self, new_id):
        self.id = new_id

    def get_id(self):
        return self.id

class UserProxy(User):
    """ Classe proxy que controla o acesso a classe User """
    def __init__(self, user):
        self._user = user  # RealSubject

    def set_id(self, new_id):
        """ 
        Intercepta a chamada ao metodo set_id 
        """
        print(f"[Proxy] Interceptando tentativa de definicao de id: {new_id}")
        if not isinstance(new_id, int) or new_id <= 0:
            raise ValueError(f"[Proxy] ERROR: ID deve ser integer e positivo.")
        print(f"[Proxy] ID alterado: {self._user.id} => {new_id}")
        self._user.set_id(new_id)

    def get_id(self):
        print("[Proxy] Lendo id usuario")
        return self._user.get_id()

    def __getattr__(self, attr):
        """ 
        Delega acesso aos outros atributos de RealObject 
        """
        return getattr(self._user, attr)


class UserFactory:  # Fabrica de usuarios
    @staticmethod
    def create(id: int) -> User:
        # return User(id, "Alice")   # Real Object
        return UserProxy(User(id, "Alice"))   # Proxy


if __name__ == "__main__":
    try:
        user = UserFactory.create(1)

        print(f"ID: {user.get_id()}")         # Interceptado pelo Proxy
        print(f"User name: {user.name}")      # Proxy delega acesso ao atributo para RealSubject
        user.set_id(2)                        # Proxy intercepta e executa validacao
        user.set_id(-1)                       # Raise ValueError
        
    except ValueError as e:
        print(e)
