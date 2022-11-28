# todo son objetos
# las funciones tambien
def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


# se puede asignar una función a una variable
mi_funcion = mayuscula

mi_funcion("python")


# también se puede pasar como argumento de una función
def una_funcion(funcion):
    return funcion


una_funcion(mayuscula("probando"))


# se pueden definir funciones dentro de otras funciones
def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula


operacion = cambiar_letras("may")

operacion("palabra")


# añadir decoradores
# la siguiente funcion añade funcionalidades a otras funciones que se le pasen como argumento
def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")

    return otra_funcion


def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


minuscula("Python")
mayuscula("Python")

# se puede poner en una variable para usarla cuando se quiera
mayuscula_decorada = decorar_saludo(mayusculas)
mayuscula("daniel")
mayuscula_decorada("daniel")

# o directamente con los decoradores
# hace que una función envuelva a otra
@decorar_saludo
def mayusculas(texto):
    print(texto.upper())


@decorar_saludo
def minusculas(texto):
    print(texto.lower())


minuscula("Python")
mayuscula("Python")
