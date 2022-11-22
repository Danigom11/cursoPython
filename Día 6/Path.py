from pathlib import Path

# devuelve una instacia con una ruta absoluta al directorio del usuario principal
base = Path.home()
print(base)

# construye objetos que responden al formato de una ruta de acceso
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
# en cada sistema operativo genera la ruta con las características que necesite
# con el separador que corresponda
print(guia)

# añadir la ruta de acceso a otra variable con otro archivo
guia2 = guia.with_name("La_Pedrera.txt")
print(guia)
print(guia2)

# cada parent va a un nivel más alto
print(guia.parent.parent.parent.parent)

# glob para enumerar todos los archivos txt de una carpeta
guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("*.txt"):
    print(txt)
# busca también archivos en subcarpetas
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

# relative_to recuperar desde una carpeta específica
guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)
