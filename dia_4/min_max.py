#Min y max, mínimo y máximo, detectar valores más bajos y más altos de un objeto

menor = min(30, 20, 100, 3209)
mayor = max(30, 20, 100, 3209)
print(menor, mayor)

lista = [30, 20, 100, 3209]
print(max(lista))

print(f' El menor es {min(lista)} y el mayor es {max(lista)}')

#Sin mayusculas para mejor busqueda, organiza en tipo orden alfabetico
nombres = ['Juan', 'Pablo', 'Carlos', 'Alicia']
print(min(nombres))

#comportamiento con los diccionarios
dic = {'c1':25, 'c2':11, 'c3':90}
print(min(dic.values()))
