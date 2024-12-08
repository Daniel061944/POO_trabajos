class Comparador:
    def __init__(self, numA,numB):
        self.numA = numA
        self.numB = numB

    def comparar(self):
        if self.numA > self.numB:
            return "A es mayor que B."
        elif self.numA < self.numB:
            return "A es menor que B."
        else:
            return "A es igual a B."

A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
comparador = Comparador(A, B)
resultado = comparador.comparar()
print(resultado)