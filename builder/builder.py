class Notebook:
    def __init__(self, gpu=None):
        self.gpu: str = gpu # possibilita inicializar a gpu default
        self.cpu = None
        self.ram = None
        self.ssd = None
        self.tela = None
    def __repr__(self):
        return f"""Notebook: {id(self)} \n
        modelo: {self.cpu} \n
        gpu: {self.gpu} \n
        ram: {self.ram} \n"""

class NoteBuilder:
    def __init__(self):
        self.notebook = Notebook()

    def add_gpu(self, gpu: str):
        self.notebook.gpu = gpu
        return self
    
    def add_ram(self, ram: str):
        self.notebook.ram = ram
        return self
    
    def set_cpu(self, cpu: str):
        self.notebook.cpu = cpu
        return self
    
    def build(self) -> Notebook:
        return self.notebook

if __name__ == "__main__":
    # usuario seleciona as opcoes
    notebook = (NoteBuilder()
                .add_gpu("RTX 4090")
                .add_ram("32GB")
                .set_cpu("Intel")
                .build()
                )
    print(notebook)

    notebook2 = (NoteBuilder()
                .set_cpu("AMD")
                .build())
    print(notebook2)

"""
    builder = NoteBuilder()
    builder.add_gpu()
    .add_ram("32GB")
    .build()
"""