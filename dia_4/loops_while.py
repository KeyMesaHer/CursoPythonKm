#While, algo se repite mientras se cumpla una condición
#break, continue, pass
#condicional else, para no ciclos eternos

monedas = 5
while monedas > 0:
    print(f' Tengo {monedas} monedas')
    #monedas = monedas - 1
    monedas -= 1
else: print('No tengo más dinero')


respuesta = 's'
while respuesta == 's':
   respuesta = input('Quieres seguir?  (s/n)')
else:
   print('Gracias')

#Pass, reserva un espacio al pgr
respuesta = 's'

while respuesta == 's':
    pass

print('Hola')

#Break y Continue
nombre = input('Ingresa tu nombre:')

for letra in nombre:
    if letra == 'r':
        break
        continue
    print(letra)



n
