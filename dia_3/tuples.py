#tupples
#ocupan menos espacio que las listas
#a prueba de daños

mi_tupple = (1,2,3,4)
t = (5, 5.6, 'ff')
print(type(mi_tupple))
print(mi_tupple[-2])

#Inmutables como los strings
#mi_tupple[0] = 5

#Anidar
tu = (1,2,3, (10, 20, 30), 4)
tu = list(tu)
tu = tuple(tu)
print(type(tu))

tup = (1,2, 3,1,)
#x,y,z = tup
#print(x,y,z)
print(tup.index(2))