mi_lista = ["a", "b", "c"]
otra_lista = ["hola", 55, 6.1]
print(type(mi_lista))

# longitud lista
resultado = len(mi_lista)
print(resultado)

# extraer un elemento
resultado = mi_lista[0]
print(resultado)

resultado = mi_lista[0:2]
print(resultado)

mi_lista3 = mi_lista + otra_lista
print(mi_lista + otra_lista)
print(mi_lista3)

# se pueden sobreescribir
mi_lista3[0] = "alfa"
print(mi_lista3)

# APPEND agregar
mi_lista3.append("último")
print(mi_lista3)

# POP saltar, eliminar
mi_lista3.pop() # elimina el último
print(mi_lista3)

eliminado = mi_lista3.pop(3)
print(mi_lista3)
print(eliminado)

# ordenar lista
# no devuelve nada, no se puede asignar a una variable
lista = ["ca", "as", "dd", "be"]
lista.sort()
print(lista)

# invertir orden
lista.reverse()
print(lista)