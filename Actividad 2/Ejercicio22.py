class InfTrabajador:
    def __init__(self, nombre, salario, num_horas):
        self.nombre = nombre
        self.salario = salario
        self.num_horas = num_horas
    
    def salario_mensual(self):
        sal_mensual = self.salario * self.num_horas
        if sal_mensual > 450000:
            return f"Nombre del Trabajador: {self.nombre}\nSalario mensual: {sal_mensual:.2f}"
        else:
            return f"Nombre del Trabajador: {self.nombre}"

nombre = input("Ingrese el nombre del trabajador: ")
salario = float(input("Ingrese el salario básico por hora: "))
num_horas = float(input("Ingrese el número de horas trabajadas: "))
trabajador1 = InfTrabajador(nombre, salario, num_horas)
resultado = trabajador1.salario_mensual()
print(resultado)
