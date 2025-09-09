from models import (
    Pessoa,
    PessoaFisica,
    PessoaJuridica,
    TipoPessoa
)

def create_pessoa(tipo: TipoPessoa, nome: str = None) -> Pessoa:
    if tipo == TipoPessoa.PF:
        return PessoaFisica(nome)
    if tipo == TipoPessoa.PJ:
        return PessoaJuridica(nome)
    else:
        raise Exception(f"{tipo} nao existe")


