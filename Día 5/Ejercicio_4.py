def contar_primos(numero):
    rango = range(2, numero)
    cantidad_primos = 0
    for num in rango:
        for num2 in range(2, num):
            contador_primo = 0
            if num % num2 == 0:
                contador_primo += 1
            if contador_primo == 2:
                break
            else:
                cantidad_primos += 1

    return cantidad_primos


print(contar_primos(5))
