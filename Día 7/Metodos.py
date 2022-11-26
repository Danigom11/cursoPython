# siempre un argumento que es obligatorio. SELF
class Pajaro:
    # ATRIBUTO DE CLASE
    alas = True

    # MÉTODO DE INSTANCIA
    # puede acceder y modificar atributos del objeto
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")
        # accede a otros métodos
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pájaro es {self.color}")

    # METODO DE CLASE
    # no necesitan una instancia para poder ejecutarse
    # no pueden acceder a los atributos de instancia
    # @ DECORADOR
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        # para modificar un atributo de la clase:
        # a través del método cls
        cls.alas = False
        print(Pajaro.alas)

    # MÉTODO ESTÁTICO
    # no se refieren a la clase ni a la instancia
    # no pueden cambiar los atributos de la clase
    # es un método para asegurarte que no modifiquen tu clase
    @staticmethod
    def mirar():
        print("El pájaro mira")


"""
piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(50)
piolin.pintar_negro()
# se puede modificar el estado de la clase
piolin.alas = False
print(piolin.alas)
"""

Pajaro.poner_huevos(3)
Pajaro.mirar()


# Ejercicio 1
class Perro:
    def ladrar(self):
        print("Guau!")


mi_perro = Perro()
mi_perro.ladrar()


# Ejercicio 2
class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")


merlin = Mago()
merlin.lanzar_hechizo()


# Ejercicio 3
class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


mi_alarma = Alarma()
mi_alarma.postergar(10)


# Ejercicio de métodos 1
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


# Ejercicio de métodos 2
class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True


# Ejercicio de métodos 3
class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
        print(self.cantidad_flechas)


yo = Personaje(10)
yo.lanzar_flecha()
yo.lanzar_flecha()
yo.lanzar_flecha()

