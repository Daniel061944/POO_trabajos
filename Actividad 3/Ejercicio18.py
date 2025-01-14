import tkinter as tk
from tkinter import messagebox
class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion = retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        descuento = salario_bruto * (self.retencion / 100)
        return salario_bruto - descuento
def calcular():
    try:
        codigo = entry_codigo.get()
        nombres = entry_nombres.get()
        horas_trabajadas = float(entry_horas_trabajadas.get())
        valor_hora = float(entry_valor_hora.get())
        retencion = float(entry_retencion.get())
        empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion)
        salario_bruto = empleado.calcular_salario_bruto()
        salario_neto = empleado.calcular_salario_neto()

        label_resultado.config(text=f"Código del empleado: {empleado.codigo}\n"
                                f"Nombres: {empleado.nombres}\n"
                                f"Salario bruto: ${salario_bruto:,.2f}\n"
                                f"Salario neto: ${salario_neto:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese datos válidos.")
root = tk.Tk()
root.title("Cálculo de Salarios")
label_codigo = tk.Label(root, text="Código del empleado:")
label_codigo.grid(row=0, column=0)
entry_codigo = tk.Entry(root)
entry_codigo.grid(row=0, column=1)
label_nombres = tk.Label(root, text="Nombres:")
label_nombres.grid(row=1, column=0)
entry_nombres = tk.Entry(root)
entry_nombres.grid(row=1, column=1)
label_horas_trabajadas = tk.Label(root, text="Horas trabajadas al mes:")
label_horas_trabajadas.grid(row=2, column=0)
entry_horas_trabajadas = tk.Entry(root)
entry_horas_trabajadas.grid(row=2, column=1)
label_valor_hora = tk.Label(root, text="Valor por hora trabajada:")
label_valor_hora.grid(row=3, column=0)
entry_valor_hora = tk.Entry(root)
entry_valor_hora.grid(row=3, column=1)
label_retencion = tk.Label(root, text="Porcentaje de retención:")
label_retencion.grid(row=4, column=0)
entry_retencion = tk.Entry(root)
entry_retencion.grid(row=4, column=1)
boton_calcular = tk.Button(root, text="Calcular", command=calcular)
boton_calcular.grid(row=5, column=0, columnspan=2)
label_resultado = tk.Label(root, text="", justify=tk.LEFT)
label_resultado.grid(row=6, column=0, columnspan=2)
root.mainloop()
