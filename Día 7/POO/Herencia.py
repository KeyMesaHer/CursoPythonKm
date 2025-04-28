#Herencia -> clase hija hereda metodos y atributos de una clase padre y sobreescribirlos
#clases que se parecen entre si pero se distinguen en algunas particularidades
#DRY: Don´t Repeat Yourself -> No crear código duplicado innecesario

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

class Pajaro(Animal):
    pass

#print(Pajaro.__bases__)
#print(Animal.__subclasses__())

piolin = Pajaro(2, 'Amarillo')
piolin.nacer()
