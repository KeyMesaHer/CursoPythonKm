serie = 'N-02'

'''if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
elif serie == 'N-03':
    print('Motorola')
else:
    print(('No existe este producto'))'''

'''match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case _:
        print('No existe este producto')'''

cliente = {'nombre': 'Keissy',
           'edad': 18,
           'ocupacion': 'desarrolladora'}

pelicula = { 'titulo': 'Matrix',
             'ficha_tecnica': {'protagonista':'Keanu Reeves',
                               'director': 'Lana y Lily Wachowsky'}}

elementos = [cliente, pelicula, 'libro']
for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print(f'{nombre} es un cliente, de {edad} años y su ocupacion es: {ocupacion}  ')
        case {'titulo': titulo,
              'ficha_tecnica': {
                  'protagonista': protagonista,
                  'director': director}}:
            print(f'Esto es una pelicula llamada {titulo}, protagonizada por {protagonista} y dirigida por {director}')
        case _:
            print('No sé que es esto')