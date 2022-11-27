class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"

    def depositar(self):
        ingreso = input("¿Cuánto quieres ingresar?: ")
        return int(ingreso)

    def retirar(self):
        retiro = input("¿Cuánto quieres retirar?: ")
        return int(retiro)


def crear_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = input("Número de cuenta: ")
    balance = input("Balance: ")
    mi_cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return mi_cliente


def inicio():
    print("Bienvenido a tu cuenta bancaria")
    print("Primero debes crear un cliente:")
    mi_cliente = crear_cliente()
    print("Que quieres hacer:")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Salir")
    cerrar_programa = False
    while cerrar_programa is False:
        print(mi_cliente)
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ingreso = mi_cliente.depositar()
            mi_cliente.balance = int(mi_cliente.balance) + int(ingreso)

        elif opcion == "2":
            retiro = mi_cliente.retirar()
            mi_cliente.balance = int(mi_cliente.balance) - int(retiro)
            if int(mi_cliente.balance) < 0:
                print("No dispones de tanto dinero")
                mi_cliente.balance = int(mi_cliente.balance) + int(retiro)
        elif opcion == "3":
            cerrar_programa = True


inicio()
