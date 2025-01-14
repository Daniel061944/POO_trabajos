import tkinter as tk
from tkinter import messagebox

class CompararNumeros:
    def __init__(self, a, b):
        self.a = a
        self.b = b 

    def comparar(self):
        if self.a > self.b:
            return "A es mayor que B"
        elif self.a < self.b:
            return "A es menor que B"
        else:
            return "A es igual a B"

def comparar():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        comparacion = CompararNumeros(a, b)
        resultado = comparacion.comparar()
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def limpiarvar():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    label_resultado.config(text="")

root = tk.Tk()
root.title("Comparación de Números")
label_a = tk.Label(root, text="Valor A:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)
label_b = tk.Label(root, text="Valor B:")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)
boton_comparar = tk.Button(root, text="Comparar", command=comparar)
boton_comparar.grid(row=2, column=0, columnspan=2)
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiarvar)
boton_limpiar.grid(row=3, column=0, columnspan=2)
label_resultado = tk.Label(root, text="", justify=tk.LEFT)
label_resultado.grid(row=4, column=0, columnspan=2)
root.mainloop()