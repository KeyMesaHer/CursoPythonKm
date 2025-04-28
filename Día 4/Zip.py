#Combina dos o más listas y las entrelaza en tuples

nombres = ['Ana', 'Hugo', 'Valeria', 'Anacleta']
edades = [65, 20, 40, 55]
ciudades = ['Alaska', 'Toronto', 'Londres', 'Luxemburgo']
combinados = list(zip(nombres, edades, ciudades))
print(combinados)

#Loop que imprime frases con elementos de listas

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

