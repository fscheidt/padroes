class PageView:
    """ singleton responsavel pela contagem de visualizacoes """

    _instance = None # representa a instancia da classe PageView
    
    def __init__(self): 
        # print("__init__")
        if not hasattr(self, "count"):
            self.count = 0

    def __new__(cls):
        """ sobrescrita do método __new__ """
        """ cls: representa a classe """
        """ metodo que aloca a memoria para a instancia """
        # print("__new__")
        if cls._instance is None:
            # super representa a super classe (Object)
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self):
        return f"page count={self.count}"
        
    def render(self):
        """ mantem contador de visualizações """
        self.count += 1

    @staticmethod
    def get_instance() -> 'PageView':
        """ ponto de acesso global """
        return PageView._instance
    
