import factory

TipoPessoa = factory.TipoPessoa

if __name__ == "__main__":
    # (SEM FACTORY)
    # cria instancia a partir da classe concreta
    # pf = PessoaFisica()

    # (COM FACTORY)
    # obter a instancia chamando o factory
    
    pf = factory.create_pessoa(TipoPessoa.PF)
    pf.nome = "Maria"
    print(pf.__dict__)
    # TODO:
    # pf.calculaIR() 

    pj = factory.create_pessoa(TipoPessoa.PJ, "SuperDia")
    print(pj.__dict__)
    # TODO:
    # pj.calculaIR()
