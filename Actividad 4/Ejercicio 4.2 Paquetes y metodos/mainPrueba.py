from ApartamentoFamiliar import ApartamentoFamiliar
from Apartaestudio import Apartaestudio

class Prueba:
    def main():
        apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
        print("--- Datos del Apartamento ---")
        apto1.calcularprecioventa(ApartamentoFamiliar.valor_area)
        apto1.imprimir()
        print()
 
        print("--- Datos del Apartaestudio ---")
        aptE1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15", 1, 1)
        aptE1.calcularprecioventa(aptE1.valor_area)
        aptE1.imprimir()

Prueba.main()
