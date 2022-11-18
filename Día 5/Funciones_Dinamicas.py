def chequear_3_cifras(lista):
    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            """Return hace un break en cuanto entra
            Sirve como elemento de corte de un bucle"""
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras


resultado = chequear_3_cifras([55, 99, 6000])
print(resultado)
"""Si no puede devolver nada devuelve un objeto vacío llamado none"""

resultado = chequear_3_cifras([555, 99, 6000])
print(resultado)

resultado = chequear_3_cifras([55, 99, 6000])
print(resultado)

resultado = chequear_3_cifras([555, 99, 600])
print(resultado)


def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma += n
    return suma


lista_numeros = [2, 4, 400]

print(suma_menores(lista_numeros))


def cantidad_pares(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n % 2 == 0:
            suma += 1
    return suma


numeros = [2, 4, 5, 6]
print(cantidad_pares(numeros))

