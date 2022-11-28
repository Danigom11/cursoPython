# GENERADOR es un tipo especial de función que en vez de devolver un valor terminado
# va produciendo ese valor poco a poco a medida que lo necesitamos
# reduce el uso de memoria
# se usa YIELD en vez de return
# esta función ya a producido el 4
def mi_funcion():
    return 4


# esta espera a que la llamen para producirlo
def mi_generador():
    yield 4


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(g)
# NEXT para que lo genere
print(next(g))


def mi_funcion2():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


def mi_generador2():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion2())
print(mi_generador2())

g2 = mi_generador2()

print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))


# se pueden poner muchos yields
def mi_generador3():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g3 = mi_generador3()

# cada next actua en un yield
print(next(g3))
# siguiente yield
print(next(g3))
# y otro yield
print(next(g3))


# Ejercicio 1
def un_generador():
    generador = 1
    while True:
        yield generador
        generador += 1


generador = un_generador()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


# Ejercicio 2
def multiplos_siete():
    numero = 7
    while True:
        yield numero
        numero += 7


generador = multiplos_siete()


# Ejercicio 3
def vidas():
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"


perder_vida = vidas()
