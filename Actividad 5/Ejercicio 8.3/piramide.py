class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_valores()

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3.0

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lado = 2.0 * self.base * self.apotema
        return area_base + area_lado

    def set_valores(self):
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()