print ("PROGRAMA PARA CALCULAR EL PROMEDIO DE 5 NUMEROS\n")

suma_numeros = 0

for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}:"))
    suma_numeros += numero 
promedio = suma_numeros / 5

print(f"\nEl promedio de los 5 números ingresados es {promedio}\n")
