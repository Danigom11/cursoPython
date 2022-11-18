mi_tuple = (1, 2, (10, 20), 4)
# con o sin paréntesis
print(type(mi_tuple))

# como consutar índice
print(mi_tuple[0])
print(mi_tuple[-1])

# son inmutables

print(mi_tuple[2][0])

# casting o sobreescribir para cambiarlo a lista
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)

# Asignar una variable a cada valor del tuple
t = (1, 2, 3)
x, y, z = t
print(x, y, z)

t = (1, 2, 3, 1)
print(len(t))
# método para contar aparciones de un valor
print(t.count(1))

# método para index
print(t.index(2))


