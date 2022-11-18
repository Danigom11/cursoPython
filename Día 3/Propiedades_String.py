nombre = "Carina"
# los strings son inmutables
n1 = "Kari"
n2 = "na"
print(n1 + n2)
print(n1 * 10)

# saltos de linea con """
poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)

# buscar algo concreto o que no está
print("agua" in poema)
print("agua" not in poema)
print("sol" in poema)
print("sol" not in poema)

# largo
print(len(poema))
