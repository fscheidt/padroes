from models import (
    Pessoa, 
    PessoaFisica, 
    PessoaJuridica
)

def create_pessoa(tipo: str, nome: str = None) -> Pessoa:
    if tipo == "PF":
        return PessoaFisica(nome)
    if tipo == "PJ":
        return PessoaJuridica(nome)
    else:
        raise Exception(f"{tipo} nao existe")


