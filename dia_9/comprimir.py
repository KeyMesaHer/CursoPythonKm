import zipfile
import shutil

'''#Crear archivo comprimido vacio
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
mi_zip.write('mi_texto_A.txt') #Meter archivo en el comprimido
mi_zip.write('mi_texto_B.txt') #Meter archivo en el comprimido

mi_zip.close()

#Descomprimir zip
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()


#Comprimir archivo
carpeta_origen = 'D:\\Documentos\\Python_curso\\dia_8'
archivo_destino = 'dia_8_comprimido'
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

#Descomprimir archivo 
shutil.unpack_archive('dia_8_comprimido.zip', 'Extracción Terminada')'''


shutil.unpack_archive('Proyecto+Dia+9.zip', 'project_day9')