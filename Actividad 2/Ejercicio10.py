class Universidad:
    def __init__(self, num_inscripcion, nombres, patrimonio, estrato):
        self.num_inscripcion = num_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato

    def calcular_pago(self):
        Pmatricula = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            i = self.patrimonio * 0.03
            Pmatricula = Pmatricula + i
        return Pmatricula

    def mostrar_informacion(self):
        valor_matricula = self.calcular_pago()
        print("Numero de inscripción:", self.num_inscripcion)
        print("Nombres:", self.nombres)
        print("Pago por matricula: $", f"{valor_matricula:,.2f}")

num_inscripcion = input("Ingrese el numero de inscripcion: ")
nombres = input("Ingrese los nombres del estudiante: ")
patrimonio = float(input("Ingrese el patrimonio del estudiante: "))
estrato = int(input("Ingrese el estrato social del estudiante: "))
estudiante = Universidad(num_inscripcion, nombres, patrimonio, estrato)
estudiante.mostrar_informacion()