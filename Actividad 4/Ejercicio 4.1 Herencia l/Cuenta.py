class Cuenta:
    def __init__(self, saldo, tasa_anual):
        self.saldo = saldo
        self.Nconsignaciones = 0
        self.Nretiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0.0

    def consignar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            self.Nconsignaciones += 1

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            self.Nretiros += 1

    def calcular_interes_mensual(self):
        interes_mensual = (self.tasa_anual / 12) * self.saldo
        self.saldo += interes_mensual

    def extracto_mensual(self):
        self.saldo -= self.comision_mensual
        self.calcular_interes_mensual()
        self.Nconsignaciones = 0
        self.Nretiros = 0

    def imprimir(self):
        print(f"Saldo: {self.saldo}")
        print(f"Número de consignaciones: {self.Nconsignaciones}")
        print(f"Número de retiros: {self.Nretiros}")
        print(f"Comisión mensual: {self.comision_mensual}")
        print(f"Tasa anual: {self.tasa_anual}")
