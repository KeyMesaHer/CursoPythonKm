import os

#ruta = os.getcwd()
'''ruta = os.chdir('D:\\Escritorio\\alternativa')
archivo = open('acrux.txt')
print(archivo.read())

archivo.close()'''

#ruta2 = os.makedirs('D:\\Escritorio\\alternativa\\otra')

ruta3 = 'D:\\Escritorio\\python\\Día 6\\archivo.txt'
elemento = os.path.dirname(ruta3) #Solo el directorio
elemento = os.path.basename(ruta3) #Solo el archivo
elemento = os.path.split(ruta3) #Toda la ruta en tupla
print(elemento)

#os.rmdir('D:\\Escritorio\\alternativa\\otra') #Eliminar un directorio

otro_archivo = open('D:\\Escritorio\\alternativa\\acrux.txt')
print(otro_archivo.read())