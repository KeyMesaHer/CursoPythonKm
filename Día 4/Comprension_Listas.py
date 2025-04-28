#Usar listas de forma más dinámica
#Menos código

lista = [letra for letra in 'pyhton'] #una letra por cada letra en palabra
print(lista)
lista = [n if n * 2 > 10 else 'no' for n in range(0, 21,2)] #no es muy legible
print(lista)

pies = [34, 40, 22, 55, 50]
metros = [talla * 3.281 for talla in pies]
print(metros)