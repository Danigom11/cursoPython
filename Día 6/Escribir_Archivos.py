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

archivo = open("mi_archivo.txt", "a")

archivo.write("Nuevo inicio de sesión")

archivo.close()

archivo = open("mi_archivo.txt", "r")

for linea in archivo:
    print(linea)

archivo.close()

mi_registro = open("registro.txt", "w")

mi_registro.close()

mi_registro = open("registro.txt", "a")

registro_ultima_sesion = ["Federico", "\t", "20/12/2021","\t", "08:17:32 hs","\t", "Sin errores de carga"]
mi_registro.writelines(registro_ultima_sesion)

mi_registro.close()

mi_registro = open("registro.txt", "r")
for p in mi_registro:
    print(p)


