import tkinter as tk
from tkinter import messagebox

class InfTrabajador:
    def __init__(self, nombre, salario, num_horas):
        self.nombre = nombre
        self.salario = salario
        self.num_horas = num_horas
    
    def salario_mensual(self):
        sal_mensual = self.salario * self.num_horas
        if sal_mensual > 450000:
            return f"Nombre del Trabajador: {self.nombre}\nSalario mensual: {sal_mensual:.2f}"
        else:
            return f"Nombre del Trabajador: {self.nombre}"

def calcular_pago():
    try:
        nombre = entry_nombre.get()
        salario = float(entry_salario.get())
        num_horas = float(entry_num_horas.get())
        trabajador = InfTrabajador(nombre, salario, num_horas)
        resultado = trabajador.salario_mensual()
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_salario.delete(0, tk.END)
    entry_num_horas.delete(0, tk.END)
    label_resultado.config(text="")

root = tk.Tk()
root.title("Cálculo de Salario de Trabajador")
label_nombre = tk.Label(root, text="Nombre del Trabajador:")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)
label_salario = tk.Label(root, text="Salario Básico por Hora:")
label_salario.grid(row=1, column=0)
entry_salario = tk.Entry(root)
entry_salario.grid(row=1, column=1)
label_num_horas = tk.Label(root, text="Número de Horas Trabajadas:")
label_num_horas.grid(row=2, column=0)
entry_num_horas = tk.Entry(root)
entry_num_horas.grid(row=2, column=1)
boton_calcular = tk.Button(root, text="Calcular Salario", command=calcular_pago)
boton_calcular.grid(row=3, column=0, columnspan=1)
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=3, column=1, columnspan=1)
label_resultado = tk.Label(root, text="", justify=tk.LEFT)
label_resultado.grid(row=4, column=0, columnspan=2)
root.mainloop()