import numeros


# funciones
# Bienvenida a farmacia
def preguntar():
    print('Bienvenido a tu farmacia')

    while True:
        print("   P: Perfumería")
        print("   F: Farmacia")
        print("   C: Cosméticos")
        try:
            mi_eleccion = input("Elige: ").upper()
            ["P", "F", "C"].index(mi_eleccion)
        except ValueError:
            print("Elige una opción correcta")
        else:
            break
    numeros.mensaje(mi_eleccion)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("¿Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()
