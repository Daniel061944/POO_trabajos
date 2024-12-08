class Promocion:
    def __init__(self, val_compra, color):
        self.val_compra = val_compra
        self.color = color.lower()

    def calcular_descuento(self):
        if self.color == "blanca":
            descuento = 0
        elif self.color == "verde":
            descuento = 0.10
        elif self.color == "amarilla":
            descuento = 0.25
        elif self.color == "azul":
            descuento = 0.50
        elif self.color == "roja":
            descuento = 1.00
        else:
            raise ValueError("El color de la bolita ingresado no es válido.")
        
        return self.val_compra * descuento

    def calcular_total(self):
        descuento = self.calcular_descuento()
        return self.val_compra - descuento

    def informacion(self):
        total_a_pagar = self.calcular_total()
        print(f"\nInformación de la compra:")
        print(f"Valor de la compra: ${self.val_compra:.2f}")
        print(f"Color de la bolita: {self.color.capitalize()}")
        print(f"Total a pagar: ${total_a_pagar:.2f}")

v_compra = float(input("Ingrese el valor de la compra: "))
color_bolita = input("Ingrese el color de la bolita sacada (blanca, verde, amarilla, azul, roja): ")
compra = Promocion(v_compra, color_bolita)
compra.informacion()