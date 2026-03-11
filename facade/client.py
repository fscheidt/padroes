from pacotes import PacoteFacade

if __name__ == "__main__":
    """ Interface "terminal" para reserva de pacotes """

    pacote = PacoteFacade()
    
    pacote.reservar(
        origem="Foz do Iguaçu",
        destino="Curitiba",
        data="2026-10-10",
        entrada="2026-10-11",
        saida="2026-10-20",
    )

