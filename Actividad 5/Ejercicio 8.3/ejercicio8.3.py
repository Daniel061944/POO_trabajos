import tkinter as tk
from tkinter import messagebox
import math

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0
        self.superficie = 0

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_valores()

    def calcular_volumen(self):
        return math.pi * self.altura * self.radio ** 2

    def calcular_superficie(self):
        area_lado_a = 2.0 * math.pi * self.radio * self.altura
        area_lado_b = 2.0 * math.pi * self.radio ** 2
        return area_lado_a + area_lado_b

    def set_valores(self):
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_valores()

    def calcular_volumen(self):
        return (4/3) * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4.0 * math.pi * self.radio ** 2

    def set_valores(self):
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_valores()

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3.0

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lado = 2.0 * self.base * self.apotema
        return area_base + area_lado

    def set_valores(self):
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas")
        self.geometry("300x200")

        btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_ventana_cilindro)
        btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_ventana_esfera)
        btn_piramide = tk.Button(self, text="Pirámide", command=self.abrir_ventana_piramide)

        btn_cilindro.pack(pady=5)
        btn_esfera.pack(pady=5)
        btn_piramide.pack(pady=5)

    def abrir_ventana_cilindro(self):
        VentanaCilindro()

    def abrir_ventana_esfera(self):
        VentanaEsfera()

    def abrir_ventana_piramide(self):
        VentanaPiramide()

class VentanaCilindro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cilindro")
        self.geometry("300x200")
        self.crear_interfaz()
    
    def crear_interfaz(self):
        tk.Label(self, text="Radio (cms):").pack()
        self.radio_entry = tk.Entry(self)
        self.radio_entry.pack()

        tk.Label(self, text="Altura (cms):").pack()
        self.altura_entry = tk.Entry(self)
        self.altura_entry.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack()
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        radio = float(self.radio_entry.get())
        altura = float(self.altura_entry.get())
        cilindro = Cilindro(radio, altura)
        self.resultado.config(text=f"Volumen: {cilindro.volumen:.2f} cm³\nSuperficie: {cilindro.superficie:.2f} cm²")

class VentanaEsfera(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Esfera")
        self.geometry("300x200")
        self.crear_interfaz()
    
    def crear_interfaz(self):
        tk.Label(self, text="Radio (cms):").pack()
        self.radio_entry = tk.Entry(self)
        self.radio_entry.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack()
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        radio = float(self.radio_entry.get())
        esfera = Esfera(radio)
        self.resultado.config(text=f"Volumen: {esfera.volumen:.2f} cm³\nSuperficie: {esfera.superficie:.2f} cm²")

class VentanaPiramide(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Pirámide")
        self.geometry("300x200")
        self.crear_interfaz()
    
    def crear_interfaz(self):
        tk.Label(self, text="Base (cms):").pack()
        self.base_entry = tk.Entry(self)
        self.base_entry.pack()

        tk.Label(self, text="Altura (cms):").pack()
        self.altura_entry = tk.Entry(self)
        self.altura_entry.pack()

        tk.Label(self, text="Apotema (cms):").pack()
        self.apotema_entry = tk.Entry(self)
        self.apotema_entry.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack()
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        base = float(self.base_entry.get())
        altura = float(self.altura_entry.get())
        apotema = float(self.apotema_entry.get())
        piramide = Piramide(base, altura, apotema)
        self.resultado.config(text=f"Volumen: {piramide.volumen:.2f} cm³\nSuperficie: {piramide.superficie:.2f} cm²")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
