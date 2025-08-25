class PageViews:

    def __init__(self):
        self.counter = 0
        
    def add_visiter(self):
        """ incrementa contador de visitantes """
        self.counter += 1
        print(self.counter)

    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance


if __name__ == "__main__":
    page = PageViews()  
    