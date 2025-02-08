class Notas:
    def __init__(self):
        self.listadeNotas = [0] * 5

    def calcular_promedio(self):
        return sum(self.listadeNotas) / len(self.listadeNotas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma_cuadrados = sum((a - promedio) ** 2 for a in self.listadeNotas)
        desviacion = (suma_cuadrados / len(self.listadeNotas)) ** 0.5
        return desviacion

    def calcular_menor(self):
        return min(self.listadeNotas)

    def calcular_mayor(self):
        return max(self.listadeNotas)
