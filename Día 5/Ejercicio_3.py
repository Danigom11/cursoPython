def cero_repetido(*args):
    contador = 0

    for numero in args:
        # if args[contador] == 0 and args[contador + 1] == 0
        if numero == 0 and contador == 0:
            contador += 1
            continue
        elif contador == 1:
            if (contador + numero) == 1:
                resultado = True
                return resultado
            contador = 0
    resultado = False
    return resultado


print(cero_repetido(5, 6, 1, 0, 0, 9, 3, 5))
print(cero_repetido(6, 0, 5, 1, 0, 3, 0, 1))
