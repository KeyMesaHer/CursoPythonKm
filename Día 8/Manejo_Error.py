'''def suma():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    suma = n1 + n2
    print(suma)
    print('Gracias por sumar' + n1)


try:
    #código que queremos probar
    suma()
except TypeError:
    #Codigo a ejecutar si hay un error
    print('Estas intentando concatenar tipos distintos')
except ValueError:
    print('Ese no es un número')
else:
    #Ejecutar si no hay un error
    print('Hiciste todo bien')

finally: #No tiene tanta aplicación
    #codigo que se va a ejecutar de todos modos
    print('Eso fue todo')
'''

def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un número: "))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero: {numero}')
            break
    print('Gracias')

pedir_numero()
