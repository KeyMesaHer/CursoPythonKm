from pathlib import Path, PureWindowsPath

#No hay que abrir (Open) y cerrar (Close) el archivo
carpeta = Path('D:/Escritorio/python/Día 6/archivo.txt')
print((carpeta.read_text()))
print((carpeta.name))
print((carpeta.suffix)) #Devuelve la terminación del archivo
print(carpeta.stem) #Devuelve el nombre del archivo

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Cool, existe')


