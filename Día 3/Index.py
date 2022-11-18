mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)
resultado = mi_texto[-2]
print(resultado)

# index busca de izquierda a derecha
resultado = mi_texto.index("n")
print(resultado)
resultado = mi_texto.index("prueba")
print(resultado)
resultado = mi_texto.index("a")
print(resultado)

# se le puede indicar desde que indice buscar y hasta donde
resultado = mi_texto.index("a", 5)
print(resultado)
resultado = mi_texto.index("a", 5, 15)
print(resultado)

# rindex busca de derecha a izquierda
resultado = mi_texto.rindex("a")
print(resultado)
