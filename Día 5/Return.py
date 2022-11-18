def multiplicar(numero1, numero2):
    """ Return devuelve un resultado """
    total = numero1 * numero2
    return total


resultado = multiplicar(2, 3)
print(resultado)


def invertir_palabra(palabra):
    return palabra.upper()[::-1]


print(invertir_palabra("hola"))
