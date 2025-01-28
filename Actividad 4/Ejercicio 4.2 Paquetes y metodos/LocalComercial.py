from Local import Local
# Clase LocalComercial (hereda de Local)
class LocalComercial(Local):
    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local, CentroComercial):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self.CentroComercial = CentroComercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self.CentroComercial}")