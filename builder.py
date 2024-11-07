class Notebook:
    def __init__(self, ram=None, ssd=None, cpu=None):
        self.ram = ram
        self.ssd = ssd
        self.cpu = cpu or "intel"

class NotebookBuilder:
    def __init__(self):
        self.note = Notebook()

    def set_ram(self, ram):
        self.note.ram = ram
        return self
    
    def set_ssd(self, ssd):
        self.note.ssd = ssd
        return self
    
    def set_cpu(self, cpu):
        self.note.cpu = cpu
        return self
    
    def build(self) -> Notebook:
        """ retorna a instancia pronta """
        # if self.ram is None:
        #     raise Exception()
        return self.note
        
if __name__ == "__main__":

    note = (NotebookBuilder()
            .set_ram(32)
            .set_ssd(512)
            .set_cpu("amd")
            .build())
    
    note2 = (NotebookBuilder()
            .set_cpu("amd")
            .build())
    


