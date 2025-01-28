from Casa import Casa
# Clase CasaRural (hereda de Casa)
class CasaRural(Casa):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos, dist_cabecera, altitud):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)
        self.dist_cabecera = dist_cabecera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self.dist_cabecera} km.")
        print(f"Altitud sobre el nivel del mar = {self.altitud} metros.")
