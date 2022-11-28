# generadores
def numero_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"


def numero_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"


def numero_cosmeticos():
    for n in range(1, 10000):
        yield f"C - {n}"


p = numero_perfumeria()
f = numero_farmacia()
c = numero_cosmeticos()


# decorador
def mensaje(eleccion):
    print(f"Su numero es: ")
    if eleccion == "P":
        print(next(p))
    elif eleccion == "F":
        print(next(f))
    else:
        print(next(c))
    print("Espere su turno y será atendido. Gracias")
