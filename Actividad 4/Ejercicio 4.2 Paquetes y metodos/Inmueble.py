# Clase padre Inmueble
class Inmueble:
    def __init__(self, identificador_inmobiliario, area, direccion):
        self.identificador_inmobiliario = identificador_inmobiliario
        self.area = area
        self.direccion = direccion
        self.precioventa = 0 

    def calcularprecioventa(self, valor_area):
        self.precioventa = self.area * valor_area
        return self.precioventa

    def imprimir(self):
        print(f"Identificador inmobiliario = {self.identificador_inmobiliario}")
        print(f"Área = {self.area}")
        print(f"Dirección = {self.direccion}")
        print(f"Precio de venta = ${self.precioventa:.2f}")