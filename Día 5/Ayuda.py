dic = {"clave1": 100, "clave2": 500}
print(dic)
# dejar raton sobre lo que se quiera investigar
# en el enlace que aparece al final es la documentación oficial
# la documentación está traducida al español
a = dic.popitem()
print(a)
print(dic)
b = dic.popitem()
print(b)
print(dic)

j = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',')
print(j)

c = 'Arthur: three!'.lstrip('Arthur: e')
print(c)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
print(conjuntos_aislados)





