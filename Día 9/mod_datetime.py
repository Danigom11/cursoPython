import datetime
from datetime import datetime
from datetime import date

"""
solo con import datetime

mi_hora = datetime.time(17, 35, 50, 1500)
print(type(mi_hora))
print(mi_hora)
print(mi_hora.min)
print(mi_hora.hour)

mi_dia = datetime.date(2025, 10, 17)
print(mi_dia)
print(mi_dia.year)
print(mi_dia.ctime())
print(mi_dia.today())
"""

# para fecha completa con dia y hora
mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 1500)
print(mi_fecha)
# reemplazar algo
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)

# calcular tiempo entre un momento y otro. Fechas u horas
nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento

print(vida)
print(vida.days)

# para contar las horas

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)
vigilia = duerme - despierta
print(vigilia)
# los segundos
print(vigilia.seconds)


# Ejercicio 1
mi_fecha = date(1999, 2, 3)
print(mi_fecha)


# Ejercicio 2
hoy = date.today()

print(hoy)


# Ejercicio 3
hora = datetime.now()
minutos = hora.minute
print(minutos)
