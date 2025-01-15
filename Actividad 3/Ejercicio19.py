import tkinter as tk
from tkinter import messagebox
import math

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def calcular_propiedades(self):
        perimetro = 3 * self.lado
        altura = (math.sqrt(3) / 2) * self.lado
        area = (self.lado * altura) / 2
        return perimetro, altura, area

def calcular():
    try:
        lado = float(entry_lado.get())
        triangulo = TrianguloEquilatero(lado)
        perimetro, altura, area = triangulo.calcular_propiedades()
        label_resultado.config(text=f"Perímetro: {perimetro:.2f} \n"
                                f"Altura: {altura:.2f} \n"
                                f"Área: {area:.2f} ")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para el lado.")

def limpiarcamp():
    entry_lado.delete(0, tk.END)
    label_resultado.config(text="")

root = tk.Tk()
root.title("Cálculo de Triángulo Equilátero")
label_lado = tk.Label(root, text="Valor del lado del triángulo:")
label_lado.grid(row=0, column=0)
entry_lado = tk.Entry(root)
entry_lado.grid(row=0, column=1)
boton_calcular = tk.Button(root, text="Calcular", command=calcular)
boton_calcular.grid(row=1, column=0)
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiarcamp)
boton_limpiar.grid(row=1, column=1)
label_resultado = tk.Label(root, text="", justify=tk.LEFT)
label_resultado.grid(row=2, column=0, columnspan=2)
root.mainloop()
