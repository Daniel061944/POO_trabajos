import tkinter as tk
from tkinter import messagebox
from notas import Notas

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.labels = []
        self.entradas = []
        for i in range(5):
            label = tk.Label(root, text=f"Nota {i+1}:")
            label.pack()
            self.labels.append(label)

            entrada = tk.Entry(root)
            entrada.pack()
            self.entradas.append(entrada)

        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.pack()

        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.pack()

        self.label_promedio = tk.Label(root, text="Promedio = ")
        self.label_promedio.pack()

        self.label_desviacion = tk.Label(root, text="Desviación estándar = ")
        self.label_desviacion.pack()

        self.label_mayor = tk.Label(root, text="Nota mayor = ")
        self.label_mayor.pack()

        self.label_menor = tk.Label(root, text="Nota menor = ")
        self.label_menor.pack()

    def calcular(self):
        try:
            notas = Notas()
            notas.listadeNotas = [float(e.get()) for e in self.entradas]

            self.label_promedio.config(text=f"El Promedio = {notas.calcular_promedio():.2f}")
            self.label_desviacion.config(text=f"La Desviación estándar = {notas.calcular_desviacion():.2f}")
            self.label_mayor.config(text=f"La Nota mayor = {notas.calcular_mayor():.2f}")
            self.label_menor.config(text=f"La Nota menor = {notas.calcular_menor():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese solo números válidos")

    def limpiar(self):
        for e in self.entradas:
            e.delete(0, tk.END)
        self.label_promedio.config(text="El Promedio = ")
        self.label_desviacion.config(text="La Desviación estándar = ")
        self.label_mayor.config(text="La Nota mayor = ")
        self.label_menor.config(text="La Nota menor = ")
