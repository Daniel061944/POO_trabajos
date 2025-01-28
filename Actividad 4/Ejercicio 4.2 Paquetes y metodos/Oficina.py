from Local import Local
# Clase Oficina (hereda de Local)
class Oficina(Local):
    valor_area = 3500000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local, es_gobierno):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self.es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self.es_gobierno}")
        print()

    def calcular_precio_venta(self, valor_area):
        precio_venta = valor_area * self.area
        print(f"Precio de venta = ${precio_venta}")
