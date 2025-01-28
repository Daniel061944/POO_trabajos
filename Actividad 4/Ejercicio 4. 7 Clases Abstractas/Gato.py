from Felino import Felino
class Gato(Felino):
    def __init__(self):
        super().__init__("Maullido", "Ratones", "Doméstico", "Felis silvestris catus")

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat