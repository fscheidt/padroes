"""
ADAPTER
Permite adaptar classes de diferentes tipos em uma mesma interface.

Exemplo: Dog, Cat
- o que possuem em comum: fazer barulho

"""
from typing import Callable, TypeVar
T = TypeVar("T")

class Dog:
    def __init__(self) -> None:
        self.name = "Dog"
    def bark(self) -> str:
        return "woof!"

class Cat:
    def __init__(self) -> None:
        self.name = "Cat"
    def meow(self) -> str:
        return "meow!"


class Adapter:
    """Adapta o objeto substituindo o metodo
    bark e meow
    """

    def __init__(self, 
                 obj: T, 
                 **adapted_methods: Callable
      ):
        """We set the adapted methods in the object's dict."""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object."""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict."""
        return self.obj.__dict__


def main():
    """ ADAPTER - add metodo make_noise """
    
    objects = []
    dog = Dog()
    cat = Cat()

    # adapta dog para reconhecer make_noise
    obj = Adapter(dog, make_noise=dog.bark)
    obj.make_noise()

    # adapta cat reconhecer make_noise
    obj2 = Adapter(cat, make_noise=cat.bark)
    obj2.make_noise()

    objects.append(dog)
    objects.append(cat)
    
    # exemplo de um array de objetos nao 
    # conhecidos em runtime
    for obj in objects:
        print(obj.name, obj.make_noise())
    

if __name__ == "__main__":
    main()
