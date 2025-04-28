#Poli -> muchos
#Morfo -> formas
#Los objetos pueden tomar diferentes formas
#Dos metodos con el mismo nombre pueden ejecutar dos cosas distintas

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')
#vaca1.hablar()
#oveja1.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla()