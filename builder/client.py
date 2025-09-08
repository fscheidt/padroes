from builder import NoteBuilder

# client.py
# RUNTIME 
if __name__ == "__main__":
    
    # instancia primeiro notebook
    notebook = (NoteBuilder()
                .add_cpu("Intel Core i5")
                .add_gpu("Nvidia 5050")
                .add_ssd("2 TB")
                .add_ram("32 GB")
                # .add_sistema("Ubuntu")
                .build()
                )
    # print(notebook.valor)
    print(notebook.__dict__)
    print(id(notebook))


    # instancia um segundo notebook:
    notebook = (NoteBuilder()
                .add_ram("16 GB")
                .add_cpu("Amd Ryzen")
                .build()
                )
    # print(notebook.valor)
    print(notebook.__dict__)
    print(id(notebook))