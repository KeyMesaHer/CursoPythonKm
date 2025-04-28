import Numeros

def menu():
    while True:
        print("P -> Perfumeria \n C -> Cosmética \n F -> Farmacia")
        try:
            opcion = input("Elija su opción: ").upper()
            ["P", "C", "F"].index(opcion)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    Numeros.texto_decorador(opcion)

def inicio():
    while True:
        menu()
        try:
            siguiente = input("Quieres sacar otro turno? S/N: ").upper()
            ["S", "N"].index(siguiente)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if siguiente == "N":
                print("ESO ES TODO POR HOY")
                break

inicio()

