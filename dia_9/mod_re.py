import re

texto = "Si necesitas ayuda llama al 911 las 24 horas del día los siete días de la semana, serviicios de ayuda online "
patron = 'ayuda'
#busqueda = re.findall(patron, texto)

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
    
texto = "Llama al 234-456-6789 ya msimo"
patron = r'(\d{3}-\d{3}-\d{4})'
resultado = re.search(patron, texto)
print(resultado.group(1))


clave = input('clave: ')
patron = r'\D{1}\w{7}'
chequear = re.search(patron, clave)
print(chequear)

texto = '4No atendemos los lunes por las tarde6'

buscar = re.search(r'lunes|martes', texto)
buscar = re.search(r'^\D', texto)
buscar = re.search(r'\D$', texto)
buscar = re.findall(r'[^\s]+', texto)
print(buscar)