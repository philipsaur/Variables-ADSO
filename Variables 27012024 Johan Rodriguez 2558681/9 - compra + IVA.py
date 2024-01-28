print ("PRGRAMA PARA CALCULAR EL COSTO TOTAL DE UNA COMPRA CON IVA DE 16%\n")
valor_unitario = float(input("Ingresa el valor unitario del producto:"))

cantidad_productos = int(input("Ingresa la cantidad de productos comprados:"))

costo_sin_iva = valor_unitario * cantidad_productos

iva = 0.16 * costo_sin_iva

total = costo_sin_iva + iva

print(f"\nEl costo total de la compra con el 16% de IVA es de {total}\n")
