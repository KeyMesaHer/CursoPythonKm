#Asignación de atributos a clases
#Atributos de clase pertenecientes a la clase, son los mismo para los que utilicen la clase
#Atributos de instancia, pueden ser distintos en cada objeto

#Atributos de instancia
class Pajaro:
    def __init__(self, color, especie): #Self es obligatorio (instancia del objeto)
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('Negro', 'Loro')
palabra = 'Hola'
print(f'Mi pajaron es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')

#Atributos de clase
class Pajaro:
    alas = True

print(Pajaro.alas)
