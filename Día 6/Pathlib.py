from pathlib import Path, PureWindowsPath

# convertir una variable en un objeto path
carpeta = Path("C:/Users/danig/PycharmProjects/pythonProject/Día 6/Prueba.txt")

# no hay que abrir y cerrar el archivo
# leer texto
print(carpeta.read_text())

# nombre archivo
print(carpeta.name)

# terminación archivo o extensión
print(carpeta.suffix)

# nombre archivo sin terminación
print(carpeta.stem)

# si existe un archivo
if not carpeta.exists():
    print("no existe")
else:
    print("si existe")

# transformar en una ruta de windows
# importar PureWindowsPath
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
