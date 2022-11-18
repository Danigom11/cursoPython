mi_set = set([1, 2, 3, 4, 5, 1, 2, 3])
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3, (10, 20)}
print(type(otro_set))
print(otro_set)

# son elementos únicos, lo que se repita lo omite
# no admite listas o diccionarios por que son mutables
# si admite tuples ya que son inmutables

# largo
print(len(mi_set))

# in, not in
print(2 in mi_set)

# unión de sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

# add
s4 = {1, 2, 3}
s4.add(4)
print(s4)

# eliminar remove si no está da error
s4.remove(2)
print(s4)

# discard elimina pero no da error si no está
s4.discard(1)
s4.discard(6)
print(s4)

# pop elimina un elemento aleatorio si no se pone posición

sorteo = s4.pop()
print(sorteo)

# clear vacía el set
s4.clear()
print(s4)
