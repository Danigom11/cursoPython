import collections
from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque

numeros = [8, 7, 6, 7, 8, 5, 4, 3, 6, 7, 8, 6, 5, 4, 6, 6]
frase = "al pan pan y al vino vino"
palabra = "mississipi"
serie = Counter([1,1,1,1,1,2,2,2,3,3,3,3,3,3,4])
# COUNTER cuenta los repetidos y los muestra como un diccionario
print(Counter(numeros))
print(Counter(palabra))
print(Counter(frase.split()))
# métodos de counter
# más comun
print(serie.most_common(2))
# convierte a una lista los elementos más comunes sin repetir
print(list(serie))

# DEFAULT DIC
mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'verde'}
# si se elige una clave inexistente da error y esto puede ser problemático
print(mi_dic['tres'])
# asi le decimos que hacer en caso de poner una clave que no tenga nada
mi_dic = defaultdict(lambda: 'no existe')
print(mi_dic["cuatro"])

# NAMED TUPLE
mi_tupla = (500, 18, 65)
# acceder a tupla a traves de índice
print(mi_tupla[1])
# acceder a traves de un nombre
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
# a traves de su nombre
print(ariel.altura)
# a traves de su índice
print(ariel[1])


# Ejercicio 1
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)


# Ejercicio 2
mi_diccionario = defaultdict(lambda: 'Valor no hallado')
mi_diccionario["edad"] = 44
print(mi_diccionario['edad'])


# DEQUE capacidad de incorporar al princio o al final a una lista
# Ejercicio 3
lista = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(lista)

