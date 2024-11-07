class Driver:
    _instance = None  # <= Singleton - atributo da classe
    def __init__(self):
        if not hasattr(self, 'name'): # executa somente uma vez
            print('init Driver')
            self.name = ""

    def __new__(cls): # cls = representa a classe Driver
        """ eh executado no comando: Driver() """
        print('new Driver')
        if cls._instance is None:  # primeira vez cria a instancia
            print("creating Singleton")
            cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == "__main__":
    driver1 = Driver() # <= chama o metodo __new__()  
    print(id(driver1))
    driver2 = Driver()
    print(id(driver2))