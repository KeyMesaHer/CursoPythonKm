#Decoradores: diferentes tipos de metodos
#Metodos de instancia los actuales
#Metodo de clases @classmethod (cls, en lugar de self) no pueden acceder a los atributos de instancia
#Metodos estaticos @staticmethod (no aceptan parametros self ni cls)


class Pajaro:

    #metodos de instancia
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print(f'Pío')
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pájaro es {self.color}')

    #Metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    #Metodos estáticos
    @staticmethod
    def mirar():
        print('El pajaro mira')

Pajaro.poner_huevos(3)
Pajaro.mirar()

