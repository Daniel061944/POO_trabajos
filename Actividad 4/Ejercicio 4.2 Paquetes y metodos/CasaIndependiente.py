from CasaUrbana import CasaUrbana
# Clase CasaIndependiente (hereda de CasaUrbana)
class CasaIndependiente(CasaUrbana):
    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)
        