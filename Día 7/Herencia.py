# DRY
# Don't Repeat Yourself
class Animal:
    # Atributo de instancia
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    # Métoto de instancia
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    # AÑADIR ATRIBUTOS A LA CLASE HIJA
    # primera forma de hacerlo
    """def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo"""

    # segunda forma de hacerlo más corta
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    # MODIFICA MÉTODO DE LA CLASE PADRE SOLO PARA LA CLASE HIJA
    def hablar(self):
        print("pio")

    # NUEVO MÉTODO
    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros")


print(Pajaro.__bases__)
print(Animal.__subclasses__())
piolin = Pajaro(2, "Amarillo", 60)

piolin.nacer()
piolin.hablar()
piolin.volar(100)
mi_animal = Animal(5, "negro")


class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("Que tal")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
# mro metod order resolution para saber el orden en el que hereda una clase
print(Nieto.__mro__)
mi_nieto.hablar()
mi_nieto.reir()


# Ejercicio 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    pass


# Ejercicio 2
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    pass


# Ejercicio 3
class Vehiculo:

    def acelerar(self):
        pass

    def frenar(self):
        pass


class Automovil(Vehiculo):
    pass


# Ejercicio 1 herencia extendida
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class Hija(Madre, Padre):
    pass


# Ejercicio 2 herencia extendida
class Vertebrado:
    vertebrado = True


class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")


class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass


# Ejercicio 3 herencia extendida
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
