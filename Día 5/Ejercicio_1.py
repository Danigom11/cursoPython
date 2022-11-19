def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    lista = [num1, num2, num3]
    lista.sort()

    if suma > 15:
        retorno = lista[2]
        return retorno
    elif suma < 10:
        retorno = lista[0]
        return retorno
    else:
        retorno = lista[1]
        return retorno


print(devolver_distintos(3, 4, 2))
