from random import choice

# Lista de palabras
lista = ['python', 'programacion', 'computo', 'lenguaje']
letras_acertadas = set()
intentos = 6

# Función para obtener una palabra al azar
def palabra_azar():
    return choice(lista)

# Función para pedir una letra
def pedir_letra():
    return input('Ingrese una letra: ').strip().lower()

# Función para verificar si la letra está en la palabra
def check_letra(letra, palabra, letras_acertadas):
    if letra in palabra:
        print(f'La letra "{letra}" es correcta y está en la palabra.')
        letras_acertadas.add(letra)
        return True
    else:
        print(f'La letra "{letra}" no se encuentra en la palabra.')
        return False

# Función para mostrar el avance del juego
def avance_juego(palabra, letras_acertadas):
    avance = [letra if letra in letras_acertadas else "_" for letra in palabra]
    print(' '.join(avance))
    return "_" not in avance  # Devuelve True si se adivinó toda la palabra

palabra = palabra_azar()

print("¡Bienvenido al juego de Ahorcadito!\n")

while intentos > 0:
    avance_juego(palabra, letras_acertadas)
    letra = pedir_letra()

    if not letra.isalpha() or len(letra) != 1:
        print("Por favor, ingresa solo una letra válida.")
        continue

    if letra in letras_acertadas:
        print("Ya has ingresado esa letra.")
        continue

    if not check_letra(letra, palabra, letras_acertadas):
        intentos -= 1
        print(f"Te quedan {intentos} intentos.")

    if avance_juego(palabra, letras_acertadas):
        print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
        break
else:
    print(f"Lo siento, se acabaron los intentos. La palabra era: {palabra}")


