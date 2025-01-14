import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa

    def calcular_hipotenusa(self):
        return self.hipotenusa

    def tipo_triangulo(self):
        if self.base == self.altura == self.hipotenusa:
            return "Equilátero"
        elif self.base == self.altura or self.base == self.hipotenusa or self.altura == self.hipotenusa:
            return "Isósceles"
        else:
            return "Escaleno"

def calcular_figura():
    try:
        figura = combo_figura.get()
        
        if figura == "Círculo":
            radio = float(entry_parametro.get())
            circulo = Circulo(radio)
            resultado = f"Área: {circulo.area():.2f} cm²\nPerímetro: {circulo.perimetro():.2f} cm"
        elif figura == "Rectángulo":
            base = float(entry_parametro.get())
            altura = float(entry_altura.get())
            rectangulo = Rectangulo(base, altura)
            resultado = f"Área: {rectangulo.area()} cm²\nPerímetro: {rectangulo.perimetro()} cm"
        elif figura == "Cuadrado":
            lado = float(entry_parametro.get())
            cuadrado = Cuadrado(lado)
            resultado = f"Área: {cuadrado.area()} cm²\nPerímetro: {cuadrado.perimetro()} cm"
        elif figura == "Triángulo Rectángulo":
            base = float(entry_parametro.get())
            altura = float(entry_altura.get())
            triangulo = TrianguloRectangulo(base, altura)
            resultado = (f"Área: {triangulo.area()} cm²\n"
                         f"Perímetro: {triangulo.perimetro()} cm\n"
                         f"Hipotenusa: {triangulo.calcular_hipotenusa():.2f} cm\n"
                         f"Tipo de triángulo: {triangulo.tipo_triangulo()}")
        
        label_resultado.config(text=resultado)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def limpiarcam():
    combo_figura.set("")
    entry_parametro.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    label_resultado.config(text="")

root = tk.Tk()
root.title("Figuras Geométricas")
label_figura = tk.Label(root, text="Seleccione una figura:")
label_figura.grid(row=0, column=0)
combo_figura = ttk.Combobox(root, values=["Círculo", "Rectángulo", "Cuadrado", "Triángulo Rectángulo"])
combo_figura.grid(row=0, column=1)
label_parametro = tk.Label(root, text="Parámetro (radio/base/lado):")
label_parametro.grid(row=1, column=0)
entry_parametro = tk.Entry(root)
entry_parametro.grid(row=1, column=1)
label_altura = tk.Label(root, text="Altura (solo para Rectángulo y Triángulo):")
label_altura.grid(row=2, column=0)
entry_altura = tk.Entry(root)
entry_altura.grid(row=2, column=1)
boton_calcular = tk.Button(root, text="Calcular", command=calcular_figura)
boton_calcular.grid(row=3, column=0)
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiarcam)
boton_limpiar.grid(row=3, column=1)
label_resultado = tk.Label(root, text="", justify=tk.LEFT)
label_resultado.grid(row=4, column=0, columnspan=2)
root.mainloop()