import os
from itertools import count
from pathlib import Path
from os import system

#Definimos la ruta de las recetas
ruta = Path(Path.home(), "Recetas")

#Le damos la bienvenida al usuario y le decimos la ruta de acceso a las recetas
print(f'Bienvenid@ al Recetario')
print(f'Todas las recetas se encuentran en la siguiente ruta: {ruta}')

#Función para contar la cantidad de recetas
def cantidad_recetas(ruta):
    count = 0
    for receta in Path(ruta).glob('**/*.txt'):
        count += 1
    return count

#Le decimos al usuario la cantidad de recetas existentes en la ruta
print(f'En este momento, el recetario tiene en total {cantidad_recetas(ruta)} recetas')

#Menú de opciones
def mostrar_menu():
    while True:
        print("Elige una opción:")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa''')

        opcion = input("Introduce un número del 1 al 6: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 6:
                return opcion

        print("Por favor, intenta de nuevo.\n")

def categorias(ruta):
    print('Categorias disponibles: ')
    categorias_ruta = Path(ruta)
    categorias_lista = []

    for indice, carpeta in enumerate(categorias_ruta.iterdir(), start=1):
        print(f"[{indice}] - {carpeta.name}")
        categorias_lista.append(carpeta)

    return categorias_lista

#Función para que el usuario escoja una categoria
def elegir_categoria(lista):
    while True:
        opcion = input("\nElige una categoría (número): ")

        if opcion.isdigit():
            indice = int(opcion)
            if 1 <= indice <= len(lista):
                return lista[indice - 1]

        print("Opción inválida. Intenta nuevamente.")

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    count = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{count}] - {receta_str}")
        lista_recetas.append(receta)
        count += 1

    return lista_recetas


def elegir_receta(lista):
    while True:
        opcion = input("\nElige una receta (número): ")

        if opcion.isdigit():
            indice = int(opcion)
            if 1 <= indice <= len(lista):
                return lista[indice - 1]

        print("Opción inválida. Intenta nuevamente.")

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(F"La categoria {categoria.name} ha sido eliminada")


def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ")


finalizar_programa = False

while not finalizar_programa:
    menu = mostrar_menu()

    if menu == 1:
        mis_categorias = categorias(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = categorias(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias = categorias(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias = categorias(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True

