import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def inicio():
    system('cls')
    print('*' * 50)
    print("*" * 5 + " Bienvenido al administrador de recetas " + "*" * 5)
    print('*' * 50)
    print("\n")
    print(f"Las recetas se enuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elige una opcion: ")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa''')
        eleccion_menu = input()
    return eleccion_menu


inicio()

menu = 0

if menu == 1:
    # mostrar categorias
    # elegir categoría
    # mostrar recetas
    # elegir recetas
    # leer receta
    # volver al inicio
    pass
elif menu == 2:
    # mostrar categorias
    # elegir categoría
    # crear receta nueva
    # volver al inicio
    pass
elif menu == 3:
    # crear categoría
    # volver inicio
    pass
elif menu == 4:
    # mostrar categorias
    # elegir categoría
    # mostrar recetas
    # elegir recetas
    # eliminar receta
    # volver al inicio
    pass
elif menu == 5:
    # mostrar categorías
    # elegir categoría
    # eliminar categoría
    # volver inicio
    pass
elif menu == 6:
    # finalizar programa
    pass

"""
# Función para la bienvenida
def bienvenida():
    print("Bienvenido a tu programa de recetas")


# Función ruta acceso recetas
def ruta_acceso_recetas(ruta):
    mi_ruta = open(ruta)
    return mi_ruta.read()


# Función total recetas
def total_recetas(ruta_acceso_abierta):
    guia = Path(Path.home(), ruta_acceso_abierta)
    numero_total_recetas = 0
    for txt in Path(guia).glob("**/*.txt"):
        print(txt)
        numero_total_recetas += 1
    return numero_total_recetas


# Función opciones
def opciones():
    print("opciones")


# Desarrollo
while not finalizar_codigo:
    bienvenida()
    print(f"Mis recetas están aquí:\n" + ruta_acceso_recetas("C:\\Recetas"))
    print(total_recetas(ruta_acceso_recetas("C:\\Recetas")))

"""
