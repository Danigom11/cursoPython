lista1 = [letra for letra in "Python"]
print(lista1)
lista2 = [n for n in range(0, 21, 2)]
print(lista2)
lista3 = [n / 2 for n in range(0, 21, 2)]
print(lista3)
lista4 = [n for n in range(0, 21, 2) if n * 2 > 10]
print(lista4)
lista5 = [n if n * 2 > 10 else "no" for n in range(0, 21, 2)]
print(lista5)

pies = [10, 20, 30, 40, 50]
metros = [pie * 3.281 for pie in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor % 2 == 0]

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(g-32)*(5/9) for g in temperatura_fahrenheit]
print(grados_celsius)
