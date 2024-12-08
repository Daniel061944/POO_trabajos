class Esfera:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def determinar_esfera_diferente(self, esferas):
        if esferas[0].peso == esferas[1].peso == esferas[2].peso:
            if esferas[3].peso > esferas[0].peso:
                return f"La esfera D es la diferente y es de mayor peso."
            else:
                return f"La esfera D es la diferente y es de menor peso."
        
        elif esferas[0].peso == esferas[1].peso == esferas[3].peso:
            if esferas[2].peso > esferas[0].peso:
                return f"La esfera C es la diferente y es de mayor peso."
            else:
                return f"La esfera C es la diferente y es de menor peso."

        elif esferas[0].peso == esferas[2].peso == esferas[3].peso:
            if esferas[1].peso > esferas[0].peso:
                return f"La esfera B es la diferente y es de mayor peso."
            else:
                return f"La esfera B es la diferente y es de menor peso."

        else:
            if esferas[0].peso > esferas[1].peso:
                return f"La esfera A es la diferente y es de mayor peso."
            else:
                return f"La esfera A es la diferente y es de menor peso."

peso_A = float(input("Ingresa el peso de la esfera A: "))
peso_B = float(input("Ingresa el peso de la esfera B: "))
peso_C = float(input("Ingresa el peso de la esfera C: "))
peso_D = float(input("Ingresa el peso de la esfera D: "))
esferas = [Esfera("A", peso_A), Esfera("B", peso_B), Esfera("C", peso_C), Esfera("D", peso_D)]
resultado = esferas[0].determinar_esfera_diferente(esferas)
print(resultado)
