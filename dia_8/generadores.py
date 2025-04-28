#Funcion que devuelve valores construidos de a poco
#yield en lugar de return

def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista

def generador():
    for x in range(1, 5):
        yield x * 10

print(mi_funcion())
print(generador())

g = generador()
print(next(g)) #Next para acceder al generador


def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))

