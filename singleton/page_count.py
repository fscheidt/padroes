class PageViews:
    """ singleton que mantem o contador de acesso """
    _instance = None  # representa um objeto da classe PageViews

    def __init__(self):
        """ método construtor """
        print("__init__")
        if not hasattr(self, "counter"):
            self.counter = 0

    @staticmethod
    def get_instance():
        """ ponto de acesso global """
        return PageViews()
        
    def add_visiter(self):
        """ incrementa contador de visitantes """
        self.counter += 1
        print(f"{self.counter=}")

    def __new__(cls): # cls == PageViews
        """ sobrescreve o metodo __new__ """
        print("__new__")
        if cls._instance is None:
            # cria instancia:
            print("creating _instance")
            cls._instance = super().__new__(cls) 
        return cls._instance


if __name__ == "__main__":
    page = PageViews()  #  page = PageViews.__init__()
    page.add_visiter()
    page.add_visiter()
    print(id(page)) # endereco de memoria

    page2 = PageViews()
    page2.add_visiter()
    print(id(page2)) # endereco de memoria

    page3 = PageViews.get_instance()
    page3.add_visiter()
    print(id(page3)) # endereco de memoria