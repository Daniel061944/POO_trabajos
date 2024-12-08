import math
class Triangulo:
    def __init__(self, l1, l2, l3):
        self.l1=l1
        self.l2=l2
        self.l3=l3

    def calcular_perimetro(self):
        return self.l1+self.l2+self.l3

    def calcular_semiperimetro(self):
        return (self.l1+self.l2+self.l3) / 2

    def calcular_area(self):
        s=self.calcular_semiperimetro()
        area = math.sqrt(s * (s - self.l1) * (s - self.l2) * (s - self.l3))
        return area

    def informacion(self):
        perimetro = self.calcular_perimetro()
        semiperimetro = self.calcular_semiperimetro()
        area=self.calcular_area()
        
        print(f"Información del triangulo:")
        print(f"Lado 1: {self.l1}")
        print(f"Lado 2: {self.l2}")
        print(f"Lado 3: {self.l3}")
        print(f"Perimetro: {perimetro}")
        print(f"Semiperimetro: {semiperimetro}")
        print(f"Area: {area:.2f}")

l1 = float(input("Ingrese el primer lado del triángulo: "))
l2 = float(input("Ingrese el segundo lado del triángulo: "))
l3 = float(input("Ingrese el tercer lado del triángulo: "))
triangulo = Triangulo(l1, l2, l3)
triangulo.informacion()