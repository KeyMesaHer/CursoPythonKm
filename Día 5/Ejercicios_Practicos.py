#Ejercicio 1
def devolver_distintos(a, b, c):
    suma = a + b + c
    lista = [a, b, c]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(3, 2, 1)
)

#Ejercicio 2

def palabra_orden(palabra):
    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista

print(palabra_orden('cascarrabias'))

#Ejercicio 3
def devolver_bool(*args):
    count = 0
    for num in args:
        if count + 1  == len(args):
            return False
        elif args[count] == 0 and args[count+1] == 0:
            return True
        else:
            count += 1

    return False

print(devolver_bool(1, 3, 5, 0, 0,  6, 2, 6))

#Ejercicio 4

def contar_primos(num):
    primos = [2]
    iteracion = 3

    if num < 2:
        return 0

    while iteracion <= num:

        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)
print(contar_primos(40))



