class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion = retencion

    def calcular_salario_neto(self):
        self.salario_bruto = self.horas_trabajadas * self.valor_hora
        descuento = self.salario_bruto * (self.retencion / 100)
        self.sn = self.salario_bruto - descuento
        return self.sn

codigo = input("Ingrese el código del empleado: ")
nombres = input("Ingrese los nombres del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas al mes: "))
valor_hora = float(input("Ingrese el valor por hora trabajada: "))
retencion = float(input("Ingrese el porcentaje de retención en la fuente: "))
empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion)
print("\nInformación del empleado:")
empleado.calcular_salario_neto()
print(f"Código del empleado: {empleado.codigo}")
print(f"Nombres: {empleado.nombres}")
print(f"Salario bruto: ${empleado.salario_bruto:.3f}")
print(f"Salario bruto: ${empleado.sn:.3f}")