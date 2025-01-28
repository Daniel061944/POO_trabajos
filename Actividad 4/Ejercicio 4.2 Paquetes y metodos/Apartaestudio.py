from Apertamento import Apartamento
# Clase Apartaestudio (hereda de Apartamento)
class Apartaestudio(Apartamento):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):
        super().__init__(identificador_inmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()