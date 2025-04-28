nombre = input("Ingresa tu nombre: ")
ventas = float(input("Ingresa tu total de ventas del mes: "))
comision = round(ventas * 13 / 100, 3)

print(f"Ok {nombre}, este mes ganaste {comision}")


