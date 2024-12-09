from math import sqrt, pi

# Definimos las clases de las figuras geometricas

class Circulo:
    def _init_(self, radio: int):
        self.radio = radio

    def calcular_area(self):
        return pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * pi * self.radio

class Cuadrado:
    def _init_(self, lado: int):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Rectangulo:
    def _init_(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class TrianguloRectangulo:
    def _init_(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return sqrt(self.base * 2 + self.altura * 2)

    def tipo_triangulo(self):
        lados = sorted([self.base, self.altura, self.calcular_hipotenusa()])
        if abs(lados[0]*2 + lados[1]2 - lados[2]*2) < 1e-9:
            return "Triángulo rectángulo"
        elif lados[0] == lados[1] == lados[2]:
            return "Triángulo equilátero"
        elif lados[0] == lados[1] or lados[1] == lados[2]:
            return "Triángulo isósceles"
        else:
            return "Triángulo escaleno"


# Nos aseguramos de que todo esté bien con las clases de las figuras geometricas

class testclasses:
    @staticmethod
    def main():
        circulo = Circulo(5)
        cuadrado = Cuadrado(4)
        rectangulo = Rectangulo(3, 3)
        triangulo = TrianguloRectangulo(3, 4)

        print(f"Círculo - Área: {circulo.calcular_area():.2f}, Perímetro: {circulo.calcular_perimetro():.2f}")
        print(f"Cuadrado - Área: {cuadrado.calcular_area()}, Perímetro: {cuadrado.calcular_perimetro()}")
        print(f"Rectángulo - Área: {rectangulo.calcular_area()}, Perímetro: {rectangulo.calcular_perimetro()}")
        print(f"Triángulo Rectángulo - Área: {triangulo.calcular_area()}, Perímetro: {triangulo.calcular_perimetro():.2f}")
        print(f"Hipotenusa: {triangulo.calcular_hipotenusa():.2f}, Tipo: {triangulo.tipo_triangulo()}")


# Ejecutamos el programa

if _name_ == "_main_":
    testclasses.main()
