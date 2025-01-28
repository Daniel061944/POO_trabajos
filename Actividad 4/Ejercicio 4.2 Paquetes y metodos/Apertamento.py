from InmuebleVivienda import InmuebleVivienda
# Clase Apartamento (hereda de InmuebleVivienda)
class Apartamento(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)

    def imprimir(self):
        super().imprimir()