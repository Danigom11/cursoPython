from random import *

# número aleatorio entre dos números indicados
aleatorio = randint(1, 50)
print(aleatorio)

# aleatorio entre dos números con muchos decimales
# se pueden indicar cuántos decimales con round
aleatorio2 = round(uniform(1, 5), 3)
print(aleatorio2)

# un número décimal entre cero y uno
aleatorio3 = random()
print(aleatorio3)

# choice un elemento de una lista aleatorio
colores = ["azul", "rojo", "verde", "amarillo"]
aleatorio4 = choice(colores)
print(aleatorio4)

# suffle mezclar, no se puede usar en strings por que son inmutables
# genera una lista in situ, no se puede almacenar en otra lista
numeros = list(range(5, 50, 5))
print(numeros)
shuffle(numeros)
print(numeros)


