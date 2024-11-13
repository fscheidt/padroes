"""
TEMPLATE LAYOUT
"""
from abc import abstractmethod, ABC
from typing import final
class BaseLayout(ABC):
    def header(self):
        # carrega header.html
        print("1. HEADER")

    @abstractmethod
    def body(self): ...

    def footer(self): 
        print("3. FOOTER")

    @final
    def render(self):
        """ METODO TEMPLATE """
        self.header() # concreto
        self.body()   # abstrata pq depende do usuario
        self.footer() # concreto

class AdminLayout(BaseLayout):
    def body(self):
        print("include admin.html")

class ClientLayout(BaseLayout):
    def header(self):
        print("include header.html")
    def body(self):
        print("include client.html")

# Aplicacao
def WebPage(layout: BaseLayout):
    layout.render()

if __name__ == "__main__":
    # if user == "admin": 
    WebPage(AdminLayout())
    # else
    print("="*40)
    WebPage(ClientLayout())
