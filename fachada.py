from booking import ReservaHotel, ReservaVoo, ReservaTransporte
class ReservaFacade:  # fachada 
    def __init__(self):
        self.aereo = ReservaVoo()
        self.hotel = ReservaHotel()
        self.transporte = ReservaTransporte()
    def reserva_pacote(self, origem, destino, data, data_volta):
        self.aereo.reservar_voo(origem, destino, data)
        self.hotel.reservar_hotel(destino, data, data_volta)
        self.transporte.reservar_transporte(destino, data)

if __name__ == "__main__":
    fachada = ReservaFacade()
    fachada.reserva_pacote(
        origem = "Foz", 
        destino = "Curitiba", 
        data = "2024-10-23",
        data_volta = "2024-10-28"
    )
