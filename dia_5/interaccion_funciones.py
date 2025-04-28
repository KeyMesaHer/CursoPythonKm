from random import shuffle

#Lista inicial
palitos = ['-', '--', '---', '----']

#Mezclar palitos
def mezclar(lista_palitos):
    shuffle(palitos)
    return lista_palitos

#Pedirle intento azar
def probar_suerte():
    intento = ''

    while intento  not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')

    return int(intento)

#Comprobar el intento
def check_intento(lista_palitos, intento):
    if lista_palitos[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')

    print(f' Te ha tocado {lista_palitos[intento - 1]}')


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
check_intento(palitos_mezclados, seleccion)
