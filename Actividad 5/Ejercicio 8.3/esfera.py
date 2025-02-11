class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_valores()

    def calcular_volumen(self):
        return (4/3) * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4.0 * math.pi * self.radio ** 2

    def set_valores(self):
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()