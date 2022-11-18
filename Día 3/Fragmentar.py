# SLICING
texto = "ABCDEFGHIJKLM"
fragmento = texto[2]
print(fragmento)
# de uno a otro sin incluir la posición indicada para el último
fragmento = texto[2:5]
print(fragmento)
# desde uno hasta el final
fragmento = texto[2:]
print(fragmento)
# hasta uno en concreto
fragmento = texto[:5]
print(fragmento)
# cada cuantos caracteres extraer e ir saltando como se indique
fragmento = texto[2:10:2]
print(fragmento)
# del cero al último saltando según lo que se diga
fragmento = texto[::3]
print(fragmento)
# para imprimir de derecha a izquierda
fragmento = texto[::-1]
print(fragmento)
frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase[0:9]
print(fragmento)