#Métodos especiales

lista = [1, 1, 1, 1, 1, 1]
print(lista)


class Objeto:
    pass

mi_objeto = Objeto()
print(mi_objeto)


class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones =  canciones

    #Definir la forma en que se manifiesta un str cada vez que se solicita
    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    #Definir que sucede si se pide el largo del objeto
    def __len__(self):
        return self.canciones

    #Eliminar e imprimir que lo eliminó
    def __del__(self):
        print('Se ha eliminado el CD')


cd = CD('Pink Floyd', 'The Wall', 24)
print(len(cd))
print(cd)