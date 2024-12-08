import math
class Triangulo:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        self.P=3*self.lado
        return self.P
    
    def Altura(self):
        return self.lado*(math.sqrt(3) / 2)
    
    def area(self):
        h=self.Altura()
        return h*self.lado/2
    
    def informacion(self):
        perimetro = self.calcular_perimetro()
        h=self.Altura()
        A=self.area()
        print(f"lado del triangulo equilatero: {self.lado}")
        print(f"El perimetro es: {self.P:.2f}")
        print(f"Salario bruto: {h:.2f}")
        print(f"Salario neto: {A:.2f}")

lado=float(input("Ingrese el lado del triángulo equilátero: "))
inf_triangulo=Triangulo(lado)
inf_triangulo.informacion()