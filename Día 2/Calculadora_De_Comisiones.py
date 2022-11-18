nombre = input("¿Cómo te llamas?\n")
ventasMes = float(input("Cuánto has vendido este mes?\n"))
resultado_comisiones = round(ventasMes * 13 / 100, 2)
print(f"Enhorabuena {nombre}, las comisiones que te corresponden para este mes son:\n {resultado_comisiones}€")