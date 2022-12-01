import re

"""
texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = 'ayuda' in texto
print(palabra)

patron = 'ayuda'

# SEARCH busca la primera vez que aparece lo que queramos buscar
busqueda = re.search(patron, texto)
print(busqueda)

# SEARCH SPAN solo la ubicación
busqueda = re.search(patron, texto)
print(busqueda.span())

# SEARCH START ubicación comienzo
busqueda = re.search(patron, texto)
print(busqueda.start())

# SEARCH END final
busqueda = re.search(patron, texto)
print(busqueda.end())

# FINDALL buscar todas las veces que aparece algo
# hace una lista con las apariciones que encuentre
busqueda = re.findall(patron, texto)
print(busqueda)
print(len(busqueda))

# FINDITER para encontrar la ubicación de cada hallazgo
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

texto = "llama al 564-565-6588 ya mismo"

# \d buscar un número de 0 a 9
patron = r'\d\d\d-\d\d\d-\d\d\d\d'

resultado = re.search(patron, texto)

print(resultado)
# GROUP para obtener el resultado concreto
print(resultado.group())

# {} poner cantidad de veces que se repite el número
patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron, texto)
print(resultado)
print(resultado.group())

# COMPILE para poder acceder a cada grupo creado ponerlos entre paréntesis
# índices aquí empiezan con el uno
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron, texto)
print(resultado)
print(resultado.group(1))
print(resultado.group(2))
print(resultado.group(3))

# para comprobar que una clave empieze con una letra y tenga 8 caracteres
'''clave = input("Clave: ")
patron = r'\D{1}\w{7}'
chequear = re.search(patron, clave)
print(chequear)'''

# operadores especiales
texto = "No atendemos los lunes por la tarde"

# O uno u otro
buscar = re.search(r'lunes|martes', texto)
print(buscar)

# PUNTO: COMODÍN cada uno que se ponga busca un espacio antes
buscar = re.search(r'......demos', texto)
print(buscar)

# ^ SI UN PATRÓN ESTÁ AL COMIENZO acento circunflejo 
# buscar si no empieza con un número
buscar = re.search(r'^\D', texto)
print(buscar)

# SI UN PATRÓN ESTÁ AL FINAL dolar
# buscar si no termina con un número
buscar = re.search(r'\D$', texto)
print(buscar)

# EXCLUIR poner expresión entre llaves rectas
# busca todos los caracteres que no sean espacios vacios
# con el signo + sigue buscando hasta que encuentra otro espacio vacio
# hace una lista de palabras sin espacios
buscar = re.findall(r'[^\s]+', texto)
print(buscar)
# texto entero sin espacios vacios
print(''.join(buscar))
"""


# Ejercicio 1
def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


verificar_email("danigom11@gmail.com")

# Ejercicio 2
def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        "No has saludado"


# Ejercicio 3
def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
