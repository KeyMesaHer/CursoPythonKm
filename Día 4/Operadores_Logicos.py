#Operadores lógicos or and y no
mi_bool = (4 < 5) and (5 > 6)
mi_bool = (4 < 5) or (5 > 6)
mi_bool = not 'a' == 'a'
mi_bool = not ('a' != 'a')
print(mi_bool)

texto = 'Esta frase es breve'
comp = ('frase' in texto) and ('breve' in texto)
print(comp)