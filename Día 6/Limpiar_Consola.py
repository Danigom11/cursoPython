from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

# hay que activar en run > debug > configuración > buscar la hoja > activar casilla windows
# cls cambia según sistema operativo o IDE
system('cls')

print(f"Tu nombre es {nombre} y tienes {edad} años")
