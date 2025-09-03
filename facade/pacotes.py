from aereo import ReservaVoo
from hotels import ReservaHotel
from transporte import ReservaTransporte

class PacoteFacade:
    """ 
    [1] FACADE
    Fornece uma interface unificada para simplificar o processo de 
    reserva de pacotes turísticos que envolvem aéreo, hospedagem e transporte
    """
    def __init__(self):
        self.aereo = ReservaVoo()
        self.hotels = ReservaHotel()
        self.transporte = ReservaTransporte()

    def reservar(self, origem, destino, data, data_entrada, data_saida):
        self.aereo.reservar_voo(origem, destino, data)
        self.hotels.reservar_hotel(destino, data_entrada, data_saida)
        self.transporte.reservar_transporte(destino, data)


