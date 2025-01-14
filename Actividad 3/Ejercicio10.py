import tkinter as tk
from tkinter import messagebox

class Estudiante:
    def __init__(self, numero_ins, nombres, patrimonio, estrato):
        self.numero_ins = numero_ins  
        self.nombres = nombres        
        self.patrimonio = patrimonio  
        self.estrato = estrato        
        self.pago_base = 50000        

    def calcular_pago(self):
        if self.patrimonio > 2000000 and self.estrato > 3:
            incremento = 0.03 * self.patrimonio  
            total_pago = self.pago_base + incremento
        else:
            total_pago = self.pago_base
        return total_pago

def calcular_pago():
    try:
        numero_ins = entry_numero_ins.get()
        nombres = entry_nombres.get()
        patrimonio = float(entry_patrimonio.get())
        estrato = int(entry_estrato.get())
        estudiante = Estudiante(numero_ins, nombres, patrimonio, estrato)
        pago = estudiante.calcular_pago()
        label_resultado.config(text=f"Inscripción: {estudiante.numero_ins}\n"
                                   f"Nombres: {estudiante.nombres}\n"
                                   f"Pago de matrícula: ${pago:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def limpiarvar():
    entry_numero_ins.delete(0, tk.END)
    entry_nombres.delete(0, tk.END)
    entry_patrimonio.delete(0, tk.END)
    entry_estrato.delete(0, tk.END)
    label_resultado.config(text="")

root = tk.Tk()
root.title("Cálculo de Pago de Matrícula")
label_numero_ins = tk.Label(root, text="Número de Inscripción:")
label_numero_ins.grid(row=0, column=0)
entry_numero_ins = tk.Entry(root)
entry_numero_ins.grid(row=0, column=1)
label_nombres = tk.Label(root, text="Nombres:")
label_nombres.grid(row=1, column=0)
entry_nombres = tk.Entry(root)
entry_nombres.grid(row=1, column=1)
label_patrimonio = tk.Label(root, text="Patrimonio:")
label_patrimonio.grid(row=2, column=0)
entry_patrimonio = tk.Entry(root)
entry_patrimonio.grid(row=2, column=1)
label_estrato = tk.Label(root, text="Estrato social:")
label_estrato.grid(row=3, column=0)
entry_estrato = tk.Entry(root)
entry_estrato.grid(row=3, column=1)
boton_calcular = tk.Button(root, text="Calcular Pago", command=calcular_pago)
boton_calcular.grid(row=4, column=0, columnspan=2)
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiarvar)
boton_limpiar.grid(row=5, column=0, columnspan=2)
label_resultado = tk.Label(root, text="", justify=tk.LEFT)
label_resultado.grid(row=6, column=0, columnspan=2)
root.mainloop()