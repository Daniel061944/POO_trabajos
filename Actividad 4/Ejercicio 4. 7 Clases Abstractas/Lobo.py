from Canido import Canido
class Lobo(Canido):
    def __init__(self):
        super().__init__("Aullido", "Carnívoro", "Bosque", "Canis lupus")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat