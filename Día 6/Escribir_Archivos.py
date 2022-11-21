# r solo leer
# w borra lo que haya y empieza desde el principio o crea un archivo si no existe
# a lleva el cursor hasta el final del archivo y empieza a escribir desde allí
# se usa por programadores para poner un registro de actividad de un programa o un log con la fecha por ejemplo
archivo = open("prueba1.txt", "w")

archivo.write("Soy el nuevo texto")
archivo.write("Sin salto de linea")
archivo.write("Con salto\n")
archivo.write("""Con salto
de
linea""")
# escribe strings seguidos sin saltos de linea
archivo.writelines(["hola", "mundo", "aquí", "estoy"])

lista = ["hola", "mundo", "aquí", "estoy"]
for p in lista:
    archivo.writelines(p + "\n")

archivo.close()
