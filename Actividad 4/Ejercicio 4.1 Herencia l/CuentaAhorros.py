from Cuenta import Cuenta

class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self.activa = saldo >= 10000

    def consignar(self, cantidad):
        if self.activa:
            super().consignar(cantidad)
            self.actualizar_estado()

    def retirar(self, cantidad):
        if self.activa and cantidad > 0:
            super().retirar(cantidad)
            self.actualizar_estado()

    def extracto_mensual(self):
        if self.Nretiros > 4:
            self.comision_mensual += 1000 * (self.Nretiros - 4)
        
        interes_mensual = (self.tasa_anual / 12) * self.saldo
        self.saldo += interes_mensual
        self.saldo -= self.comision_mensual
        self.actualizar_estado()

    def actualizar_estado(self):
        self.activa = self.saldo >= 10000

    def imprimir(self):
        print(f"Saldo = ${self.saldo:.3f}")
        print(f"Comisión mensual = ${self.comision_mensual:.1f}")
        print(f"Número de transacciones = {self.Nconsignaciones + self.Nretiros}")
