def suma(*args):
    return sum(args)


print(suma(5, 6, 7, 6, 22, 456))


# Ejercicio 1
def suma_cuadrados(*args):
    total = 0
    for valor in args:
        valor *= valor
        total += valor
    return total


print(suma_cuadrados(1, 2, 3))


# Ejercicio 2
def suma_absolutos(*args):
    total = 0
    for valor in args:
        if valor < 0:
            valor *= -1
            total += valor
            continue
        total += valor
    return total


print(suma_absolutos(2, 3, 5, -7))


# Ejercicio 3

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"


print(numeros_persona("Daniel", 2, 3, 4))
