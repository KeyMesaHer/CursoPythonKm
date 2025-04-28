diccionario = { 'color':'rojo', 'animal':'cangrejo', 'nombre':'Cangrejo Rojo', 'familia':'crustaseos'}
print(diccionario)

resultado = diccionario['color']
print(resultado)

cliente = {'Nombre':'Juan', 'Apellido': 'Fuentes', 'Peso':70, 'Talla':1.67}
consulta = (cliente['Apellido'])
print(consulta)

dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':300}}
print(dic['c3']['s2'])

prueba_dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(prueba_dic['c1'][0].upper())

dic2 = {1:'a', 2:'b'}
print(dic2)
#Agregar al dicc
#dic2[3] = "B"
print(dic2)
print(dic2.keys())
print(dic2.values())
print(dic2.items())