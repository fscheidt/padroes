from models import (
    Pessoa, 
    PessoaFisica, 
    PessoaJuridica
)
from enum import Enum

class TipoPessoa(Enum):
    PF = "PF"
    PJ = "PJ"

def create_pessoa(tipo: str, nome: str = None) -> Pessoa:
    if tipo == "PF":
        return PessoaFisica(nome)
    if tipo == "PJ":
        return PessoaJuridica(nome)
    else:
        raise Exception(f"{tipo} nao existe")


