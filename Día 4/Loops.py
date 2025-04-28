#Bucles
#Objetos iterable

#LOOP FOR
lista = ['a', 'b', 'c', 'd']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'Letra:{numero_letra}: {letra}')

nombres = ['Pablito', 'Pepito', 'Luis', 'Julia', 'Peranito']
for nombre in nombres:
    if nombre.startswith('P'):
        print(nombre)
    else:
        print('Nombre que no comienza con P')

numeros = [1, 2, 3 , 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

palabra = 'python'

for letra in palabra:
    print(letra)

#No es necesaria la variable siempre
for letra in 'python':
    print(letra)

for objeto in [[1, 2], [2, 3], [3, 4]]:
    print(objeto)

dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic:
    print(item)
for item in dic.items():
    print(item)