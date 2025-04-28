#Aprendiendo a usar listas
mi_lista = ["a", "b", "c"]
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
#otra_lista = ["Hola", 55, 5.6]
result = len(mi_lista)
result = mi_lista[0]
print(result)
print(mi_lista3)

#Las listas si son mutables
mi_lista3[0]= "alfa"
#Modificar lista de origen
mi_lista3.append('g')
#Eliminar elemento
mi_lista3.pop()
print(mi_lista3)

eliiminado = mi_lista3.pop(3)
print(eliiminado)

#Ordenar las listas
lista = ['Karen', 'Alejandra', 'Sofia' , 'Kenai']
lista.sort()
print(lista)

#Sort no devuelve nada, por lo que no se puede asignar como valor
nueva_lista = lista.sort()
print(nueva_lista)

#Metodo reverse, tampoco almacena nada
lista.reverse()
print(lista)

