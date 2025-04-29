from datetime import datetime, date

mi_hora = datetime.time(17, 35)
mi_dia = datetime.date(2025, 10, 17)
print(mi_hora)
print(mi_dia.today())

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
print(mi_fecha.replace(month= 11))

nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 10)
vida = defuncion - nacimiento
print(vida.days) #Ver solo los días


despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)
vigilia = duerme - despierta
print(vigilia)
print(vigilia.seconds) #mostrar la cantidad de segundos entre tiempos



