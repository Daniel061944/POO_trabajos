import os
import tkinter as tk
from tkinter import messagebox

base_datos = "amigos.txt"

def agregar_amigo():
    codigoAmigo = entrada_codigoAmigo.get()
    nombreAmigo = entrada_nombreAmigo.get()
    if codigoAmigo and nombreAmigo:
        with open(base_datos, "a") as archivo:
            archivo.write(f"{codigoAmigo}!{nombreAmigo}\n")
        messagebox.showinfo("Éxito", "Amigo agregado exitosamente.")
        entrada_codigoAmigo.delete(0, tk.END)
        entrada_nombreAmigo.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un código y un nombre.")

def leer_amigo():
    termino_busqueda = entrada_codigoAmigo.get() or entrada_nombreAmigo.get()
    if termino_busqueda:
        try:
            with open(base_datos, "r") as archivo:
                for linea in archivo:
                    codigoAmigo, nombreAmigo = linea.strip().split("!")
                    if termino_busqueda == codigoAmigo:
                        entrada_nombreAmigo.delete(0, tk.END)
                        entrada_nombreAmigo.insert(0, nombreAmigo)
                        return
                    elif termino_busqueda == nombreAmigo:
                        entrada_codigoAmigo.delete(0, tk.END)
                        entrada_codigoAmigo.insert(0, codigoAmigo)
                        return
            messagebox.showwarning("Advertencia", "Amigo no encontrado.")
        except FileNotFoundError:
            messagebox.showwarning("Advertencia", "No hay amigos registrados.")
    else:
        messagebox.showwarning("Advertencia", "Ingrese un código o un nombre para buscar.")

def actualizar_amigo():
    codigoAmigo = entrada_codigoAmigo.get()
    nombreAmigo = entrada_nombreAmigo.get()
    if codigoAmigo and nombreAmigo:
        try:
            with open(base_datos, "r") as archivo:
                lineas = archivo.readlines()
            with open(base_datos, "w") as archivo:
                for linea in lineas:
                    if linea.startswith(codigoAmigo + "!"):
                        archivo.write(f"{codigoAmigo}!{nombreAmigo}\n")
                    else:
                        archivo.write(linea)
            messagebox.showinfo("Éxito", "Amigo actualizado exitosamente.")
        except FileNotFoundError:
            messagebox.showwarning("Advertencia", "No hay amigos registrados.")
    else:
        messagebox.showwarning("Advertencia", "Ingrese un código y un nombre.")

def eliminar_amigo():
    codigoAmigo = entrada_codigoAmigo.get()
    if codigoAmigo:
        try:
            with open(base_datos, "r") as archivo:
                lineas = archivo.readlines()
            with open(base_datos, "w") as archivo:
                for linea in lineas:
                    if not linea.startswith(codigoAmigo + "!"):
                        archivo.write(linea)
            messagebox.showinfo("Éxito", "Amigo eliminado exitosamente.")
        except FileNotFoundError:
            messagebox.showwarning("Advertencia", "No hay amigos registrados.")
    else:
        messagebox.showwarning("Advertencia", "Ingrese un código.")

def limpiar_entradas():
    entrada_codigoAmigo.delete(0, tk.END)
    entrada_nombreAmigo.delete(0, tk.END)

# Interfaz gráfica
root = tk.Tk()
root.title("Friend Schedule")

# Ajuste de espacio en los campos de entrada
tk.Label(root, text="Code:", padx=10, pady=10).grid(row=0, column=0)
tk.Label(root, text="Name:", padx=10, pady=10).grid(row=1, column=0)

entrada_codigoAmigo = tk.Entry(root, width=30)
entrada_nombreAmigo = tk.Entry(root, width=30)
entrada_codigoAmigo.grid(row=0, column=1, padx=10, pady=10)
entrada_nombreAmigo.grid(row=1, column=1, padx=10, pady=10)

# Alinear botones en una sola fila con espaciado equidistante
boton_frame = tk.Frame(root)
boton_frame.grid(row=2, column=0, columnspan=2, pady=10)

botones = [
    ("Create", agregar_amigo),
    ("Read", leer_amigo),
    ("Update", actualizar_amigo),
    ("Delete", eliminar_amigo),
    ("Clear", limpiar_entradas)
]

for i, (texto, comando) in enumerate(botones):
    tk.Button(boton_frame, text=texto, width=12, command=comando).grid(row=0, column=i, padx=10)

root.mainloop()







