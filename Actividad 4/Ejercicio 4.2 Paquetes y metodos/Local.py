from Inmueble import Inmueble
# Case Local (hereda de Inmueble)
class Local(Inmueble):
    class Tipo:
        INTERNO = 'Interno'
        CALLE = 'Calle'

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local):
        super().__init__(identificador_inmobiliario, area, direccion)
        self.tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self.tipo_local}")