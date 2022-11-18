monedas = 5
# diferencia con for es que depende de la dinámica del código que se siga repitiendo
# con for está claramente determinado
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo más dinero")

respuesta = "s"

# while respuesta == "s":
#   respuesta = input("¿Quieres seguir? (s/n)")
# else:
#    print("Gracias")

respuesta2 = "s"
# pass si aun no sabemos que queremos que haga el loop ponemos pass
# es para el programador
# guarda el lugar, reserva un espacio para el programador
# while respuesta2 == "s":
#    pass

# break y continuo
nombre = input("Tu nombre es: ")
for letra in nombre:
    if letra == "r":
        break
    if letra == "s":
        continue
    print(letra)
