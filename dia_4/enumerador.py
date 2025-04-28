#enumerate
lista = ['a', 'b', 'c']

for indice,item in enumerate(lista):
    print(indice, item)

for indice, item in enumerate(range(50, 55)):
    print(indice, item)

mis_tupples = list(enumerate(lista))
print(mis_tupples[1][0])

#Obtener acceso a los índices de un objeto iterable.