from CasaUrbana import CasaUrbana
# Clase CasaConjuntoCerrado (hereda de CasaUrbana)
class CasaConjuntoCerrado(CasaUrbana):
    valor_area = 2500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos, valor_administracion, piscina, campos_deportivos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)
        self.valor_administracion = valor_administracion
        self.piscina = piscina
        self.campos_deportivos = campos_deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = {self.valor_administracion}")
        print(f"¿Tiene piscina? = {self.piscina}")
        print(f"¿Tiene campos deportivos? = {self.campos_deportivos}")