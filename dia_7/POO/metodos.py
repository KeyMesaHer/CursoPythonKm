#Definir metodos que le den funcioalidades a las clases

class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'Pío, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')


piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(200)


