from factory_pessoa import create_pessoa

if __name__ == "__main__":
    # (SEM FACTORY)
    # cria instancia a partir da classe concreta
    # pf = PessoaFisica()

    # (COM FACTORY)
    # obter a instancia chamando o factory
    pf = create_pessoa("PF")
    pf.nome = "Maria"
    print(pf)
    # TODO:
    # pf.calculaIR() 

    pj = create_pessoa("PJ", "SuperDia")
    print(pj)
    # TODO:
    # pj.calculaIR()
