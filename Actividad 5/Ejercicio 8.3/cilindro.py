class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_valores()

    def calcular_volumen(self):
        return math.pi * self.altura * self.radio ** 2

    def calcular_superficie(self):
        area_lado_a = 2.0 * math.pi * self.radio * self.altura
        area_lado_b = 2.0 * math.pi * self.radio ** 2
        return area_lado_a + area_lado_b

    def set_valores(self):
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()
