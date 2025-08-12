from factory_pessoa import (
    create_pessoa, TipoPessoa
)
if __name__ == "__main__":
    # (SEM FACTORY)
    # cria instancia a partir da classe concreta
    # pf = PessoaFisica()

    # (COM FACTORY)
    # obter a instancia chamando o factory
    pf = create_pessoa(TipoPessoa.PF.value)
    pf.nome = "Maria"
    print(pf)
    # TODO:
    # pf.calculaIR() 

    pj = create_pessoa(TipoPessoa.PJ.value, "SuperDia")
    print(pj)
    # TODO:
    # pj.calculaIR()
