def numero_primo(numero):
    numeros_dentro_de_numero = range(2, numero)
    contador = 0
    for num in numeros_dentro_de_numero:
        if numero % num == 0:
            contador += 1
            return False
    return True


def contar_primos(numero):
    cantidad_primos = 0
    rango_busqueda_primos = range(2, numero)
    if numero < 2:
        return 0
    for numero_busqueda in rango_busqueda_primos:
        if numero_primo(numero_busqueda):
            cantidad_primos += 1
    return cantidad_primos


print(contar_primos(7))
