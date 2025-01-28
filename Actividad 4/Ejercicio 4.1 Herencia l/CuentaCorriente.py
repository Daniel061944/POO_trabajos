from Cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self.sobregiro = 0.0

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                super().retirar(cantidad)
            else:
                self.sobregiro += cantidad - self.saldo
                self.saldo = 0
                self.Nretiros += 1

    def consignar(self, cantidad):
        if cantidad > 0:
            if self.sobregiro > 0:
                if cantidad >= self.sobregiro:
                    cantidad -= self.sobregiro
                    self.sobregiro = 0
                else:
                    self.sobregiro -= cantidad
                    cantidad = 0
            super().consignar(cantidad)
    
    def extracto_mensual(self):
        super().extracto_mensual()

    def imprimir(self):
        super().imprimir()
        print(f"Valor de sobregiro: {self.sobregiro}")
        print(f"Transacciones totales: {self.Nconsignaciones + self.Nretiros}")
