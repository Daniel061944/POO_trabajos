class Comparador:
    def __init__(self, esf_A,esf_B,esf_C):
        self.esf_A = esf_A
        self.esf_B = esf_B
        self.esf_C = esf_C 

    def comparar(self):
        if self.esf_A > self.esf_B and self.esf_A > self.esf_C:
            return "La esfera A es la de mayor peso."
        
        if self.esf_B > self.esf_A and self.esf_B > self.esf_C:
            return "La esfera B es la de mayor peso."
        
        elif self.esf_C > self.esf_A and self.esf_C > self.esf_B:
            return "La esfera C es la de mayor peso."
        
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))
comparar = Comparador(A, B, C)
resultado = comparar.comparar()
print(resultado)