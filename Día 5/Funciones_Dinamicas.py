def check_3_cifras(lista):

    lista_3_cifras = []

    for num in lista:
        if num in range(100, 1000):
            lista_3_cifras.append(num)
        else:
            pass
    return lista_3_cifras

#suma = 586 + 402
resultado = check_3_cifras([555, 98, 600])
print(resultado)

#Ejemplo sistema para desempacar tuples

precios_cafe = [('capuchino',1.34),('Expreso', 4.98), ('Moka', 2.34)]

def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f' El cafe más caro es {cafe} cuyo precio es {precio}')
