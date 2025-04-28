import os
import shutil
import send2trash

'''archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())'''

#shutil.move('curso.txt', 'D:\\Escritorio\\python')
#send2trash.send2trash('curso.txt')

ruta = 'D:\\Documentos\\v3acrux'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f' En la carpeta: {ruta} ')
    print(f'Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')

