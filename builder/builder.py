from models import Notebook

"""
Builder:
Padrão de projeto Criacional
"""

# builder.py
class NoteBuilder():
    """ Constroi objetos da classe Notebook """
    def __init__(self):
        self.note = Notebook()

    def add_ram(self, ram: str):
        self.note.valor += 1250
        self.note.ram = ram
        return self
    
    def add_gpu(self, gpu: str):
        self.note.valor += 2050
        self.note.gpu = gpu
        return self
    
    def add_cpu(self, cpu: str):
        self.note.valor += 150
        self.note.cpu = cpu
        return self
    
    def add_ssd(self, ssd: str) -> "NoteBuilder":
        self.note.valor += 350 # TODO: buscar valor do item
        self.note.ssd = ssd
        return self

    def build(self) -> Notebook:
        return self.note

