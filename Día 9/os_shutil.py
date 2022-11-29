import os
import shutil
import send2trash

# para saber donde estoy
print(os.getcwd())

# crear un archivo
archivo = open('curso.txt', 'w')
archivo.write('Texto de prueba')
archivo.close()

# para ver directorio desde python
print(os.listdir())

# SHUTIL
# mover archivo
# shutil.move('curso.txt', "C:\\Users\\danig\\PycharmProjects\\pythonProject\\Día 9\\mover")

# eliminar archivo
# 3 modos

# eliminar un archivo en una ruta que se le provea
# os.unlink()

# eliminar una carpeta vacía
# os.rmdir()

# eliminar una carpeta con lo que haya. Irreversible. Peligroso de usar
# shutil.rmtree()

# Para eliminar y enviar a la papelera de reciclaje
# instalar pip install send2trash
send2trash.send2trash('curso.txt')

# WALK
# recorrer todos los directorios carpetas y subcarpetos que encuentre al pasarle una ruta
# crea un objeto. es un generador, no crea nada hasta que se le pida
print(os.walk("C:\\Users\\danig\\PycharmProjects\\pythonProject\\Día 9"))
# como pedir los datos
ruta = "C:\\Users\\danig\\PycharmProjects\\pythonProject\\Día 9"
# primero almacena ruta, luego las subcarpetas, y luego los archivos
# crea tuplas con estos tres tipos de información
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        if arch.startswith("2015"):
            print(f'\t{arch}')
    print('\n')
