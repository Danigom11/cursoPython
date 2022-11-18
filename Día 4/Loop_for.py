lista = ["a", "b", "c"]

for letra_lista in lista:
    numero_letra = lista.index(letra_lista) + 1
    print(f"Letra {letra_lista} en posición {numero_letra}")

lista2 = ["pablo", "laura", "fede", "luis", "julia"]

for nombre in lista2:
    if nombre.startswith("l"):
        print(nombre)
    else:
        print("nombre que no comienza con L")

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

palabra = "python"

for letra in palabra:
    print(letra)

for letra in "prueba":
    print(letra)

for elemento in [[1, 2], [3, 4], [5, 6]]:
    print(elemento)

for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

dic = {"clave1": "a", "clave2": "b", "clave3": "c"}
for objeto in dic:
    print(objeto)
for valor in dic.values():
    print(valor)
for completo in dic.items():
    print(completo)
for a, b in dic.items():
    print(a, b)
