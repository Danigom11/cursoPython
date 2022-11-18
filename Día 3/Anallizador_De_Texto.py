texto = input("Introduce el texto que quieras:\n").lower()
print("Ahora dime 3 letras:")
primeraLetra = input("Primera letra: ").lower()
segundaLetra = input("Segunda letra: ").lower()
terceraLetra = input("Tercera letra: ").lower()

totalLetraUno = texto.count(primeraLetra)
print(f"La primera letra {primeraLetra} se repite {totalLetraUno} veces")

totalLetraDos = texto.count(segundaLetra)
print(f"La primera letra {segundaLetra} se repite {totalLetraDos} veces")

totalLetraTres = texto.count(terceraLetra)
print(f"La primera letra {terceraLetra} se repite {totalLetraTres} veces")

textoPalabras = texto.split()
print(f"El texto tiene {len(textoPalabras)} palabras")

print(f"Primera letra del texto: {texto[0]}")
print(f"Última letra del texto: {texto[-1]}")
print(f"Texto al revés: {texto[::-1]}")
textoPalabras.reverse()
texto_invertido = " ".join(textoPalabras)
print(f"Texto con las palabras al reves: '{texto_invertido}'")

buscar_python = "python" in texto
dic = {True: "si", False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuetra en el texto")



