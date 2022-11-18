import random
from random import shuffle
from random import randint
from random import choice

"""
# Lista inicial
palitos = ["-", "--", "---", "----"]


# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle intento
def probar_suerte():
    intento = ""

    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un número del 1 al 4: ")

    return int(intento)


# Comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == "-":
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento - 1]}")


# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados, seleccion)
"""


# Ejercicio 1
def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


num1, num2 = lanzar_dados()

print(evaluar_jugada(num1, num2))

# Ejercicio 2
lista_numeros = [1, 2, 15, 7, 2]


def reducir_lista(lista):
    lista_sin_repetidos = []
    elemento_mas_alto = 0
    for numero in lista:
        if numero not in lista_sin_repetidos:
            lista_sin_repetidos.append(numero)
        if numero > elemento_mas_alto:
            elemento_mas_alto = numero
    lista_sin_repetidos.remove(elemento_mas_alto)
    return lista_sin_repetidos


def promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma / len(lista)


print(promedio(reducir_lista(lista_numeros)))

# Ejercicio 3
lista_numeros = [1, 2, 15, 7, 2, 8]


def lanzar_moneda():
    moneda = random.choice(["Cara", "Cruz"])
    return moneda


def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista


probar_suerte(lanzar_moneda(), lista_numeros)
