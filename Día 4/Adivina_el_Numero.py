from random import *

nombre = input("¿Cómo te llamas? ")
print(f"\nBueno, {nombre}, he pensado un número entre 1 y 100.\n"
      f"Tienes solo ocho intentos para adivinarlo.")
numero_aleatorio = randint(1, 100)

intentos = 1

while intentos < 9:
    numero = input("Escribe un número: ")
    numero = int(numero)
    if numero == numero_aleatorio:
        print(
            f"!Acertaste!\n "
            f"Mi número era el {numero_aleatorio}.\n "
            f"Número de intentos que has necesitado para adivinarlo: {intentos}")
        break
    elif numero < 1 or numero > 100:
        print("El número debe estar entre 1 y 100")
    elif numero < numero_aleatorio:
        print("Mi número es mayor")
        print(f"Llevas {intentos} intentos\n")
        intentos += 1
    elif numero > numero_aleatorio:
        print("Mi número es menor")
        print(f"Llevas {intentos} intentos\n")
        intentos += 1
else:
    print("Que pena... Agotaste tus ocho intentos.")
    print(f"Mi número era: {numero_aleatorio}")
