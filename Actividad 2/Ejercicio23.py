import math
class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_d(self):
        return self.b**2 - 4 * self.a * self.c

    def resolver(self):
        d = self.calcular_d()
        if self.a == 0:
            return "Esto no es una ecuación de segundo grado."
        if d > 0:
            x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(d)) / (2 * self.a)
            return f"Las soluciones son reales y distintas: x1 = {x1:.2f}, x2 = {x2:.2f}"
        elif d == 0:
            x = -self.b / (2 * self.a)
            return f"La solución es real y doble: x = {x:.2f}"
        else:
            parte_real = -self.b / (2 * self.a)
            parte_imaginaria = math.sqrt(abs(d)) / (2 * self.a)
            return (f"Las soluciones son complejas: "
                    f"x1 = {parte_real:.2f} + {parte_imaginaria:.2f}i, "
                    f"x2 = {parte_real:.2f} - {parte_imaginaria:.2f}i")
        
a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
c = float(input("Ingrese el valor de C: "))
ecuacion = EcuacionSegundoGrado(a, b, c)
resultado = ecuacion.resolver()
print(resultado)