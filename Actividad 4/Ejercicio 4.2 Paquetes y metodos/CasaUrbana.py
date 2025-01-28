from Casa import Casa
# Clase CasaUrbana (hereda de Casa)
class CasaUrbana(Casa):
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)