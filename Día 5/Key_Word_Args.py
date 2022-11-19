# Args con diccionarios
# se define con dos asteriscos y la palabra que sea
# por convencion kwargs

def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total


print(suma(x=3, y=5, z=2))

""" el orden de lo atributos debe ser como sigue"""


def suma2(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [100, 200, 300, 400]
kwargs = {"x": "uno", "y": "2", "z": "tres"}

suma2(15, 50, args, kwargs)
# para desempacar listas y diccionarios
suma2(15, 50, *args, **kwargs)


# Ejercicio 1
def cantidad_atributos(**kwargs):
    total = 0
    for atributo in kwargs:
        total += 1
    return total


# Ejercicio 2
def lista_atributos(**kwargs):
    lista = []
    for atributo in kwargs.values():
        lista.append(atributo)
    return lista


# Ejercicio 3
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre, valor in kwargs.items():
        print(f"{nombre}: {valor}")


describir_persona("María", color_ojos="azules", color_pelo="rubio")
