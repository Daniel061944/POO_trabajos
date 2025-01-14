import tkinter as tk
from tkinter import messagebox
import math

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def resolver_ecuacion(self):
        discriminante = self.b**2 - 4*self.a*self.c
        if discriminante > 0:
            x1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return f"Las soluciones son: x1 = {x1:.2f} y x2 = {x2:.2f}"
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return f"La solución única es: x = {x:.2f}"
        else:
            return "La ecuación no tiene soluciones reales."

def calcular_soluciones():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        ecuacion = EcuacionSegundoGrado(a, b, c)
        soluciones = ecuacion.resolver_ecuacion()
        label_resultado.config(text=soluciones)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def limpiarcam():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    label_resultado.config(text="")

root = tk.Tk()
root.title("Resolución de Ecuación de Segundo Grado Ax^2+Bx+C=0")
label_a = tk.Label(root, text="Valor de A:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)
label_b = tk.Label(root, text="Valor de B:")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)
label_c = tk.Label(root, text="Valor de C:")
label_c.grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)
boton_calcular = tk.Button(root, text="Calcular Soluciones", command=calcular_soluciones)
boton_calcular.grid(row=3, column=0, columnspan=2)
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiarcam)
boton_limpiar.grid(row=4, column=0, columnspan=2)
label_resultado = tk.Label(root, text="", justify=tk.LEFT)
label_resultado.grid(row=5, column=0, columnspan=2)
root.mainloop()