mi_lista = [1, 1, 1, 1, 1, 1, 1]
print(mi_lista)


class Objeto:
    pass


mi_objeto = Objeto()
print(mi_objeto)


# Como usar las funciones básicas de python como len, print... en mis objetos
class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # cada vez que se llame a STR en relación con las instancias de esta clase
    # aquí definimos como se comportará.
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    # lo mismo para LEN o cualquier otro método
    def __len__(self):
        return self.canciones

    # para DEL añade un comportamiento extra a la clase DEL
    def __del__(self):
        print("Se ha eliminado el CD")


mi_cd = CD('Pink Floyd', 'The Wall', 24)

# usar STR con un objeto (solo con llamarlo con print se convierte a string)
print(str(mi_cd))
# usamos LEN con un objeto
print(len(mi_cd))
# DEL elimina un objeto o instancia
del mi_cd


# Ejercicio 1
class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'


mi_libro = Libro("El quijote", "Cervantes", 1000)
print(mi_libro)


# Ejercicio 2
class Libro2():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return int(self.cantidad_paginas)


mi_libro2 = Libro2("El quijote", "Cervantes", 1000)
print(len(mi_libro2))


# Ejercicio 3
class Libro3():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")


mi_libro3 = Libro3("El quijote", "Cervantes", 1000)
del mi_libro3