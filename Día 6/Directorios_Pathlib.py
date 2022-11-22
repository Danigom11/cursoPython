import os
from pathlib import Path

# MÓDULO PATHLIB
# getcwd es obtener ruta actual current working directory
ruta = os.getcwd()
print(ruta)

# chdir change directory cambiar directorio
ruta = os.chdir("C:\\Users\\danig\\PycharmProjects\\pythonProject\\Día 6\\Nueva carpeta para directorios")
archivo = open("archivo_en_otra_carpeta.txt", "w")
print(archivo)
print(ruta)
archivo.close()

# crear carpeta
ruta2 = os.makedirs("C:\\Users\\danig\\PycharmProjects\\pythonProject\\Día 6\\Nueva carpeta para directorios\\carpeta_creada")

# recibir por separado ruta de nombre de archivo
ruta3 = "C:\\Users\\danig\\PycharmProjects\\pythonProject\\Día 6\\Nueva carpeta para directorios\\carpeta_creada\\archivo_en_otra_carpeta.txt"
elemento = os.path.basename(ruta3)
print(elemento)
elemento2 = os.path.dirname(ruta3)
print(elemento2)
# convierte ruta y nombre de archivo en una tupla
elemento3 = os.path.split(ruta3)
print(elemento3)

# eliminar una carpeta
os.rmdir("C:\\Users\\danig\\PycharmProjects\\pythonProject\\Día 6\\Nueva carpeta para directorios")

# abrir un archivo de otra carpeta
otro_archivo = open("C:\\Users\\danig\\PycharmProjects\\pythonProject\\Día 6\\Prueba")
print(otro_archivo.read())

# para que sirva en otros ordenadores
# importar path de pathlib
# incluso sin el c:\
carpeta = Path("/Users/danig/PycharmProjects/pythonProject/Día 6/Nueva carpeta para directorios")
# / es para concatenar rutas
# al poner la ruta de acceso al archivo a través de path cualquier sistema lo puede entender
archivo = carpeta / "otro_archivo.txt"

# se puede hacer en una sola linea
carpeta = Path("/Users/danig/PycharmProjects/pythonProject/Día 6/Nueva carpeta para directorios") / "otro_archivo.txt"

mi_archivo = open(archivo)
print(mi_archivo)






