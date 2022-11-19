def separadora(palabra):
    lista = []
    for letra in palabra:
        lista.append(letra)

    lista_ordenada = list(set(lista))
    lista_ordenada.sort()
    return lista_ordenada


print(separadora("Hcccolaaaa"))
