mi_archivo = open('archivo.txt')
#print(mi_archivo.read())
'''una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.lower())

una_linea = mi_archivo.readline()
print(una_linea)'''

'''for l in mi_archivo:
    print(f'Aquí dice: {l} ')'''

#Solo archivos pequeños
todas = mi_archivo.readlines()
todas.pop()
print(todas)

mi_archivo.close()
