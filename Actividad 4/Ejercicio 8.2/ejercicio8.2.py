import tkinter as tk
from tkinter import messagebox

class Persona:
    """
    Clase que modela una persona con nombre, apellidos, teléfono y dirección.
    """
    def __init__(self, nombre, apellidos, telefono, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion
    
    def __str__(self):
        """
        Retorna una representación en texto de la Persona.
        Aquí combinamos los atributos para mostrarlo en la lista.
        """
        return f"{self.nombre}-{self.apellidos}-{self.telefono}-{self.direccion}"


class ListaPersonas:
    """
    Clase que administra una lista (vector) de objetos Persona.
    """
    def __init__(self):
        self.lista_personas = []

    def anadir_persona(self, persona):
        """
        Agrega una persona a la lista.
        """
        self.lista_personas.append(persona)

    def eliminar_persona(self, indice):
        """
        Elimina la persona en la posición 'indice' de la lista,
        si el índice es válido.
        """
        if 0 <= indice < len(self.lista_personas):
            self.lista_personas.pop(indice)

    def borrar_lista(self):
        """
        Elimina (vacía) por completo la lista de personas.
        """
        self.lista_personas.clear()


class VentanaPrincipal(tk.Tk):
    """
    Ventana principal de la aplicación que gestiona:
    - La captura de datos de una persona.
    - El almacenamiento en una lista.
    - Las acciones de eliminar elementos y borrar la lista completa.
    """
    def __init__(self):
        super().__init__()
        
        # Creamos el objeto ListaPersonas
        self.lista = ListaPersonas()
        
        # Configuración de la ventana
        self.title("Personas")
        self.geometry("270x350")
        self.resizable(False, False)
        # (opcional) Centrar en la pantalla
        # self.eval('tk::PlaceWindow . center')
        
        # Inicializamos la interfaz
        self.iniciar_componentes()
    
    def iniciar_componentes(self):
        """
        Crea y ubica todos los componentes gráficos (Labels, Entries, Botones, Listbox, etc.)
        """
        # Usaremos place() para ubicar de forma similar a la posición absoluta de Java Swing
        
        # --- Variables de texto para los campos ---
        self.nombre_var = tk.StringVar()
        self.apellidos_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.direccion_var = tk.StringVar()
        
        # --- Etiquetas y campos de texto ---
        # Nombre
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.place(x=20, y=20)
        
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre_var)
        self.entry_nombre.place(x=105, y=20, width=135, height=23)
        
        # Apellidos
        self.label_apellidos = tk.Label(self, text="Apellidos:")
        self.label_apellidos.place(x=20, y=50)
        
        self.entry_apellidos = tk.Entry(self, textvariable=self.apellidos_var)
        self.entry_apellidos.place(x=105, y=50, width=135, height=23)
        
        # Teléfono
        self.label_telefono = tk.Label(self, text="Teléfono:")
        self.label_telefono.place(x=20, y=80)
        
        self.entry_telefono = tk.Entry(self, textvariable=self.telefono_var)
        self.entry_telefono.place(x=105, y=80, width=135, height=23)
        
        # Dirección
        self.label_direccion = tk.Label(self, text="Dirección:")
        self.label_direccion.place(x=20, y=110)
        
        self.entry_direccion = tk.Entry(self, textvariable=self.direccion_var)
        self.entry_direccion.place(x=105, y=110, width=135, height=23)
        
        # --- Botón Añadir ---
        self.boton_anadir = tk.Button(self, text="Añadir", command=self.anadir_persona)
        self.boton_anadir.place(x=105, y=150, width=80, height=23)
        
        # --- Lista (Listbox) y Scrollbar ---
        self.listbox_personas = tk.Listbox(self, selectmode=tk.SINGLE)
        
        # Scrollbar vertical
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.listbox_personas.yview)
        self.listbox_personas.config(yscrollcommand=self.scrollbar.set)
        
        # Ubicamos la lista y el scrollbar
        self.listbox_personas.place(x=20, y=190, width=200, height=80)
        self.scrollbar.place(x=220, y=190, width=20, height=80)
        
        # --- Botón Eliminar ---
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_persona)
        self.boton_eliminar.place(x=20, y=280, width=80, height=23)
        
        # --- Botón Borrar Lista ---
        self.boton_borrar_lista = tk.Button(self, text="Borrar Lista", command=self.borrar_lista)
        self.boton_borrar_lista.place(x=120, y=280, width=120, height=23)
    
    def anadir_persona(self):
        """
        Crea un objeto Persona con los datos de los Entry y lo agrega a la ListaPersonas.
        También añade una representación en el Listbox.
        """
        # Creamos el objeto Persona
        p = Persona(
            self.nombre_var.get(),
            self.apellidos_var.get(),
            self.telefono_var.get(),
            self.direccion_var.get()
        )
        
        # Lo agregamos a la lista interna
        self.lista.anadir_persona(p)
        
        # Añadimos la cadena de texto al listbox
        self.listbox_personas.insert(tk.END, str(p))
        
        # Limpiamos los campos de texto
        self.nombre_var.set("")
        self.apellidos_var.set("")
        self.telefono_var.set("")
        self.direccion_var.set("")
    
    def eliminar_persona(self):
        """
        Elimina la persona seleccionada (tanto del Listbox como de la lista interna).
        Si no se seleccionó nada, muestra un mensaje de error.
        """
        # Obtenemos el índice seleccionado
        seleccion = self.listbox_personas.curselection()
        if seleccion:
            indice = seleccion[0]
            # Eliminamos del listbox
            self.listbox_personas.delete(indice)
            # Eliminamos de la lista interna
            self.lista.eliminar_persona(indice)
        else:
            messagebox.showerror("Error", "Debe seleccionar un elemento")
    
    def borrar_lista(self):
        """
        Elimina todas las personas de la lista interna y limpia el Listbox.
        """
        self.lista.borrar_lista()
        self.listbox_personas.delete(0, tk.END)


def main():
    """
    Punto de entrada de la aplicación.
    """
    ventana = VentanaPrincipal()
    ventana.mainloop()


if __name__ == "__main__":
    main()
