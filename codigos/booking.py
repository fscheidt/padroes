class ReservaVoo:
    def reservar_voo(self, origem, destino, data):
        print(f"ReservaVoo: Reservando voo de {origem} para {destino} na data {data}.")

class ReservaHotel:
    def reservar_hotel(self, destino, data_entrada, data_saida):
        print(f"ReservaHotel: Reservando hotel em {destino} de {data_entrada} até {data_saida}.")

class ReservaTransporte:
    def reservar_transporte(self, destino, data):
        print(f"ReservaTransporte: Reservando transporte no destino {destino} para a data {data}.")
