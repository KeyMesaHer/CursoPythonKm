#crear métodos propios, bloques de codigo que se pueden ejecutar y llamar muchas veces sin necesidad de repetirlos
#def

def crear_nombre1 (nombre):
    '''Esta función es para saludar personas'''
    print(f'Hola {nombre}')
crear_nombre1('Keissy')

#intento mío
def crear_nombre ():
    '''Esta función es para saludar personas'''
    nombre = (input('Ingresa tu nombre: '))
    print(f'Hola {nombre}')

crear_nombre()