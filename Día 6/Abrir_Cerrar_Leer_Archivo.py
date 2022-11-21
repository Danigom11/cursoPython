mi_archivo = open("Prueba.txt")

print(mi_archivo)

# Convierte cada linea en una lista
todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)

for linea in mi_archivo:
    print("Aquí dice: " + linea)



# Lee una linea. Pone un punto al finalizarla. Si se vuelve a llamar coge la segunda linea y así sucesivamente
una_linea = mi_archivo.readline()
print(una_linea.upper())  # en mayusculas

una_linea = mi_archivo.readline()
print(una_linea.rstrip())  # quita el enter del final

una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo.close()
