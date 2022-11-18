nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42, 55]
ciudades = ["Lima", "Madrid", "Mexico"]

# une listas y llega hasta el tamaño de la lista más corta
combinados = list(zip(nombres, edades, ciudades))
print(combinados)

# se usa por ejemplo para hacer frases que contengan todos los elementos de las listas
for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

numero = [1, 2, 3, 4, 5]
espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
numeros = list(zip(numero, espanol, portugues, ingles))
print(numeros)



