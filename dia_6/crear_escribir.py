#Cambios directamente guardados en el archivo original
#Modos de apertura: r/read, w/write, a/write al final del archivo
archivo = open('archivo.txt', 'w')
archivo.write('Soy el nuevo texto\n')
archivo.write('''Hola Mundo
soy Keissy''')
#archivo.writelines(['hola', 'mundo', 'soy', 'yo'])
lista = ['hola', 'mundo', 'soy', 'yo']
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()