# siempre un argumento que es obligatorio. SELF
class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Métodos de instancia
    # puede acceder y modificar atributos del objeto
    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")
        # accede a otros métodos
        self.piar()


    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pájaro es {self.color}")


piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(50)
piolin.pintar_negro()
# se puede modificar el estado de la clase
piolin.alas = False
print(piolin.alas)


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
