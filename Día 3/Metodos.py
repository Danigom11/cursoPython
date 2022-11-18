texto = "Este es el texto de Federico"
resultado = texto
print(resultado)

# MAYÚSCULAS
resultado = texto.upper()
print(resultado)
resultado = texto[2].upper()
print(resultado)

# MINÚSCULAS
resultado = texto.lower()
print(resultado)

# SPLIT separar
resultado = texto.split()
print(resultado)
resultado = texto.split("t")
print(resultado)

# JOIN unir
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)
e = "-".join([a, b, c, d])
print(e)

# FIND
# diferencia con index es que index da error si no está el caracter
# find no da error. da -1
resultado = texto.find("s")
print(resultado)

# REPLACE dos parámetros: palabra a sustituir y por lo que sustituye
resultado = texto.replace("Federico", "todos")
print(resultado)
resultado = texto.replace("e", "x")
print(resultado)