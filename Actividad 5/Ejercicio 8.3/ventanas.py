class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas")
        self.geometry("300x200")

        btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_ventana_cilindro)
        btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_ventana_esfera)
        btn_piramide = tk.Button(self, text="Pirámide", command=self.abrir_ventana_piramide)

        btn_cilindro.pack(pady=5)
        btn_esfera.pack(pady=5)
        btn_piramide.pack(pady=5)

    def abrir_ventana_cilindro(self):
        VentanaCilindro()

    def abrir_ventana_esfera(self):
        VentanaEsfera()

    def abrir_ventana_piramide(self):
        VentanaPiramide()

class VentanaCilindro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cilindro")
        self.geometry("300x200")
        self.crear_interfaz()
    
    def crear_interfaz(self):
        tk.Label(self, text="Radio (cms):").pack()
        self.radio_entry = tk.Entry(self)
        self.radio_entry.pack()

        tk.Label(self, text="Altura (cms):").pack()
        self.altura_entry = tk.Entry(self)
        self.altura_entry.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack()
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        radio = float(self.radio_entry.get())
        altura = float(self.altura_entry.get())
        cilindro = Cilindro(radio, altura)
        self.resultado.config(text=f"Volumen: {cilindro.volumen:.2f} cm³\nSuperficie: {cilindro.superficie:.2f} cm²")

class VentanaEsfera(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Esfera")
        self.geometry("300x200")
        self.crear_interfaz()
    
    def crear_interfaz(self):
        tk.Label(self, text="Radio (cms):").pack()
        self.radio_entry = tk.Entry(self)
        self.radio_entry.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack()
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        radio = float(self.radio_entry.get())
        esfera = Esfera(radio)
        self.resultado.config(text=f"Volumen: {esfera.volumen:.2f} cm³\nSuperficie: {esfera.superficie:.2f} cm²")

class VentanaPiramide(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Pirámide")
        self.geometry("300x200")
        self.crear_interfaz()
    
    def crear_interfaz(self):
        tk.Label(self, text="Base (cms):").pack()
        self.base_entry = tk.Entry(self)
        self.base_entry.pack()

        tk.Label(self, text="Altura (cms):").pack()
        self.altura_entry = tk.Entry(self)
        self.altura_entry.pack()

        tk.Label(self, text="Apotema (cms):").pack()
        self.apotema_entry = tk.Entry(self)
        self.apotema_entry.pack()

        tk.Button(self, text="Calcular", command=self.calcular).pack()
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        base = float(self.base_entry.get())
        altura = float(self.altura_entry.get())
        apotema = float(self.apotema_entry.get())
        piramide = Piramide(base, altura, apotema)
        self.resultado.config(text=f"Volumen: {piramide.volumen:.2f} cm³\nSuperficie: {piramide.superficie:.2f} cm²")