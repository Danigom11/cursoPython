def suma():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)


try:
    # Código que queremos probar
    suma()
except TypeError:
    # Código a ejecutar si hay un error
    print("Intentas concatenar tipos distintos")
except ValueError:
    print("Ese no es un número")
else:
    # Código a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    # Código que se va a ejecutar de todos modos
    # Poco frecuente
    print("Eso fue todo")


def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un número: "))
        except:
            print("Ese no es un número")
        else:
            print(f"Ingresaste el número {numero}")
            break

    print("Gracias")


pedir_numero()

# Ejercicio 1
"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def suma(num1, num2):
    try:
        print(num1 + num2)
    except:
        print("Error inesperado")


# Ejercicio 2
"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def cociente(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


# Ejercicio 3
"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
