# funciones encargadas de abrir archivos o eliminarlos
def abrir_archivo(ruta, nombre_archivo):
    print("Poner código correspondiente")


def eliminar_archivo(ruta, nombre_archivo):
    print("Poner código correspondiente")


# Ejercicio 1
def abrir_leer(archivo):
    mi_archivo = open(archivo)
    return mi_archivo.read()


# Ejercicio 2
def sobreescrir(archivo):
    mi_archivo = open(archivo, "w")
    mi_archivo.write("contenido eliminado")


# Ejercicio 3
def registro_error(archivo):
    aniade_linea_final = open(archivo, "a")
    aniade_linea_final.write("se ha registrado un error de ejecución")
