var1 = True
var2 = False
print(type(var1))
print(var1)

numero = 5 > 2 + 3
print(type(numero))
print(numero)

# los operadores de comparación siempre resultan en booleanos
# se puede poner tambien bool pero no es necesario
numero = bool(5 > 6)
print(numero)
numero = bool()
print(numero)

lista = [1,2,3,4]
control = 5 in lista
print(type(control))
print(control)
