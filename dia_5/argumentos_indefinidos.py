#*args
def suma(*args):
    '''total = 0
    for arg in args:
        total += arg
    return total'''
    return sum(args)

print(suma(5, 6, 8, 1, 10, 500))

#**kwargs: convenciones
def resta(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total -= valor

    return total

print(resta(x=3, y=5, z=2))

def prueba(num1, num2, *args, **kwargs):

    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'Arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [1, 2, 3, 500]
kwargs = {'x':'Uno', 'y':'Dos', 'z':'Tres'}
prueba(15, 50, *args, **kwargs)
