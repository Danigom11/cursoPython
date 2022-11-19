# Args con diccionarios

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
