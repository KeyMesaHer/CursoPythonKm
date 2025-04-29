def perfumeria():
    for num in range (1, 100):
        yield f"P - {num}"


def cosmetica():
    for num in range (1, 100):
        yield f"C - {num}"


def farmacia():
    for num in range (1, 100):
        yield f"F - {num}"

perfu = perfumeria()
cosmetic = cosmetica()
farma = farmacia()


def texto_decorador(texto):
    print('Su turno es: ')
    if texto == 'F':
        print(next(farma))
    elif texto == 'P':
        print(next(perfu))
    else:
        print(next(cosmetic))
    print('Será atentido en un momento')
