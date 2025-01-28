from Apertamento import Apartamento
# Clase ApartamentoFamiliar (hereda de Apartamento)
class ApartamentoFamiliar(Apartamento):
    valor_area = 2000000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, valoradmin):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)
        self.valoradmin = valoradmin

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = {self.valoradmin}")