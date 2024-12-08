class Empresa:
    def __init__(self, ventas1, ventas2, ventas3, salario):
        self.ventas1 = ventas1
        self.ventas2 = ventas2
        self.ventas3 = ventas3
        self.salario = salario

    def calcular_totales(self):
        return self.ventas1 + self.ventas2 + self.ventas3

    def calcular_incentivo(self, ventas):
        ventas_totales = self.calcular_totales()
        porcentaje_ventas = ventas / ventas_totales
        if porcentaje_ventas > 0.33:
            return self.salario * 0.20
        return 0

    def calcular_salario_final(self):
        incentivo1 = self.calcular_incentivo(self.ventas1)
        incentivo2 = self.calcular_incentivo(self.ventas2)
        incentivo3 = self.calcular_incentivo(self.ventas3)
        
        salario_final1 = self.salario + incentivo1
        salario_final2 = self.salario + incentivo2
        salario_final3 = self.salario + incentivo3
        
        return salario_final1, salario_final2, salario_final3

    def mostrar_resultados(self):
        salario1, salario2, salario3 = self.calcular_salario_final()
        print(f"\nResultados finales:")
        print(f"Departamento 1: Salario total {salario1:.2f}")
        print(f"Departamento 2: Salario total {salario2:.2f}")
        print(f"Departamento 3: Salario total {salario3:.2f}")

ventas1 = float(input("Ingrese las ventas del departamento 1: "))
ventas2 = float(input("Ingrese las ventas del departamento 2: "))
ventas3 = float(input("Ingrese las ventas del departamento 3: "))
salario = float(input("Ingrese el salario de los vendedores: "))
empresa = Empresa(ventas1, ventas2, ventas3, salario)
empresa.mostrar_resultados()