from InmuebleVivienda import InmuebleVivienda
# Clase Casa (hereda de InmuebleVivienda)
class Casa(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)
        self.numero_pisos = numero_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self.numero_pisos}")