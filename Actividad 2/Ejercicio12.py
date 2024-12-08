class Trabajador:
    def __init__(self, nombres, h_trabajadas, v_hora):
        self.nombres = nombres
        self.h_trabajadas = h_trabajadas
        self.v_hora = v_hora

    def calcular_salario(self):
        horas_normales = min(self.h_trabajadas, 40) 
        horas_extras = max(0, self.h_trabajadas - 40) 
        salario_normal = horas_normales * self.v_hora
        if horas_extras <= 8:
            salario_extras = horas_extras * (self.v_hora * 2)
        else:
            salario_extras = (8 * (self.v_hora * 2)) + ((horas_extras - 8) * (self.v_hora * 3))

        return salario_normal + salario_extras

    def informacion(self):
        salario = self.calcular_salario()
        print(f"Nombre del trabajador: {self.nombres}")
        print(f"Salario devengado: ${salario:,.2f}")

nombres = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
valor_hora = float(input("Ingrese el valor recibido por una hora normal de trabajo: "))
trabajador1 = Trabajador(nombres, horas_trabajadas, valor_hora)
trabajador1.informacion()
