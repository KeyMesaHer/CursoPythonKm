from random import *

intentos = 0
num_ingresado = 0
num_aleatorio = randint (1, 100)
nombre_usuario = input('Ingresa tu nombre: ')

print(f'Hola {nombre_usuario}, he pensado un número entre 1 y 100 y tienes solo 8 intentos para adivinar cuál crees que es el número')

while intentos < 8:
    num_ingresado = int(input('Cuál crees que es el número?: '))
    intentos += 1
    if num_ingresado < num_aleatorio:
        print('Respuesta incorrecta, has elegido un número menor')
    elif num_ingresado > num_aleatorio:
        print('Respuesta incorrecta, has elegido un número mayor')
    else:
        print(f'Has acertado el número secreto, has ganado después de {intentos}')

if num_ingresado != num_aleatorio:
    print(f"Se han agotado los intentos. El numero era {num_aleatorio}")



