#Según se cumpla una condición se ejecute un código
#If, elif and else
#Sintaxis: if condicion:
#   print (no olvidar la tabulación)
from operator import truediv

if 10 > 10:
    print("Es correcto")
else:
    print("Es incorrecto")

mascota = 'perro'
if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No sé que animal tienes')

edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')

