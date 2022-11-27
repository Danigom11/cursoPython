# objetos de diferentes clases pueden compartir el mismo nombre de métodos
# y luego puedes llamar esos métodos del mismo nombre desde el mismo lugar
# pero aplicado a diferentes objetos
class Vaca:

    # CONSTRUCTOR
    def __init__(self, nombre):
        self.nombre = nombre

    # MÉTODO
    def hablar(self):
        print(self.nombre + " dice muuu")


class Oveja:

    # CONSTRUCTOR
    def __init__(self, nombre):
        self.nombre = nombre

    # MÉTODO
    def hablar(self):
        print(self.nombre + " dice beee")


# INSTANCIA U OBJETO
vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

animales = [vaca1, oveja1]

# se ejecuta el método que se llama igual pero hace cosas diferentes
for animal in animales:
    animal.hablar()


# no importa la forma o el tipo del objeto
# como comparten el mismo nombre de método se pueden llamar aunque hagan cosas diferentes
def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)

# Ejercicio 1
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

print(len(palabra))
print(len(lista))
print(len(tupla))


# Ejercicio 2
class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


mi_mago = Mago()
mi_arquero = Arquero()
mi_samurai = Samurai()

personajes = [mi_arquero, mi_mago, mi_samurai]
for personaje in personajes:
    personaje.atacar()


# Ejercicio 3
class Mago():
    def defender(self):
        print("Escudo mágico")


class Arquero():
    def defender(self):
        print("Esconderse")


class Samurai():
    def defender(self):
        print("Bloqueo")


def personaje_defender(personaje):
    personaje.defender()
