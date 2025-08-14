import models
from enum import Enum

class TipoPessoa(str, Enum):
    PF = "PF"
    PJ = "PJ"

def create_pessoa(tipo: TipoPessoa, nome: str = None) -> models.Pessoa:
    if tipo == TipoPessoa.PF:
        return models.PessoaFisica(nome)
    if tipo == TipoPessoa.PJ:
        return models.PessoaJuridica(nome)
    else:
        raise Exception(f"{tipo} nao existe")


