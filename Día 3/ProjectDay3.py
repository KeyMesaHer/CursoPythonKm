texto = input('Ingrese un texto:')
texto = texto.lower()

letras= []
print('Ahora vas a ingresar 3 letras de tu preferencia')
letras.append(input('Ingrese una letra').lower())
letras.append(input('Ingrese una letra').lower())
letras.append(input('Ingrese una letra').lower())

cantidad = texto.count(letras[0])
cantidad2 = texto.count(letras[1])
cantidad3 = texto.count(letras[2])


print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad} veces")
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad2} veces")
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad3} veces")


palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} en tu texto")

letra_i = texto[0]
letra_f = texto[-1]
print(f"La letra inicial es {letra_i} y la letra final es {letra_f}")


palabras.reverse()
invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reves va a decir: {invertido}")

buscar = 'pyhton' in texto
dic = {True: 'Si', False: 'No'}
print(f"La palabra 'Python' {dic[buscar]} se encuentra en el texto")