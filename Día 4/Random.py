#Generación de números aleatorios
#Method randint: numero entero aleatorio, libreria random
#Importación de metodos, sintaxis : from random import randint
#Randint, uniform, random, choice, shuffle

from random import *

aleatorio = randint(1, 50 ) #Intengers
print(aleatorio)

aleatorio = round(uniform(1, 50), 1) #Floats
print(aleatorio)

aleatorio = random() #Siempre da la fracción de un entero
print(aleatorio)

#Los strings también son pasibles a este sistema
colores = ['azul', 'amarillo', 'lila', 'rojo', 'verde']
aleatorio = choice(colores)
print(aleatorio)

#Orden aleatorio de una lista
numeros = list(range(5, 50, 5))
shuffle(numeros) #no se puede almacenar en una lista, se genera in situ
print(numeros)




