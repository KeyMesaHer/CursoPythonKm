#Metodos heredados iguales, heredados modificados, propios

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo =  altura_vuelo


    #Herencia modificada
    def hablar(self):
        print('Pio')

    #Nuevos métodos no heredados
    def volar(self, metros):
        print(f'El pájaro vuela {metros} metros')


piolin = Pajaro(2, 'Amarillo', 200)
mi_animal = Animal(5, 'negro')
piolin.volar(100)
piolin.hablar()


#Con la herencia multiple podemos heredar de varias clases
class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print('Jaja')

    def hablar(self):
        print('Que tal?')


class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

#En la herencia multiple, se hereda en el orden de busqueda
mi_nieto = Nieto()
mi_nieto.reir()
mi_nieto.hablar()
print(Nieto.__mro__)
