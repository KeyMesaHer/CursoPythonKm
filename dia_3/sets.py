mi_set = set([1,2,3,4,5])
print(type(mi_set))

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

#No listas, no indexes

print(len(mi_set))

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#Añadir
s1.add(4)
print(s1)

#Eliminar
s1.remove(3)
print(s1)

#Descartar
s1.discard(6)
print(s1)

#eliminar aleatorio
s1.pop()
print(s1)

#limpiar
s1.clear()
print(s1)
