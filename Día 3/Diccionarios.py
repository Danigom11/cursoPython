diccionario = {"c1": "valor1", "c2": "valor2"}
print(type(diccionario))
print(diccionario)
# las claves no se pueden repetir
# los valores si se pueden repetir
resultado = diccionario["c1"]
print(resultado)

cliente = {"nombre": "Juan", "apellido": "Fuentes", "peso": 88, "talla": 1.76}
consulta = (cliente["apellido"])
print(consulta)

# diccionario con listas y diccionario
dic = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}
print(dic["c2"])
print(dic["c2"][1])
print(dic["c3"])
print(dic["c3"]["s2"])

dic2 = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dic2["c2"][1].upper())

# agregar elementos
dic3 = {1: "a", 2: "b"}
print(dic3)

dic3[3] = "c"
print(dic3)

dic3[3] = "C"
print(dic3)

# conocer llaves, elementos y completo
print(dic3.keys())
print(dic3.values())
print(dic3.items())



