class ComparadorNumeros:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def validar_diferentes(self):
        return self.num1 != self.num2 and self.num1 != self.num3 and self.num2 != self.num3
    
    def encontrar_mayor(self):
        if self.num1 > self.num2 and self.num1 > self.num3:
            return self.num1
        elif self.num2 > self.num1 and self.num2 > self.num3:
            return self.num2
        else:
            return self.num3
        
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
comparador = ComparadorNumeros(num1, num2, num3)
if comparador.validar_diferentes():
    mayor = comparador.encontrar_mayor()
    print(f"El número mayor es: {mayor}")
else:
    print("Error: Los números ingresados deben ser diferentes.")
