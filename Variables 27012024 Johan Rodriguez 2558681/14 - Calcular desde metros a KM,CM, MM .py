print("PROGRAMA QUE PERMITE CALCULAR DESDE METROS A KM, CM, MM \n")

distancia_metros = float(input("Ingresa la distancia en metros: "))

distancia_kilometros = distancia_metros / 1000
distancia_centimetros = distancia_metros * 100
distancia_milimetros = distancia_metros * 1000

print(f"\n{distancia_metros} metros es igual a:")
print(f"{distancia_kilometros} kilómetros")
print(f"{distancia_centimetros} centímetros")
print(f"{distancia_milimetros} milímetros\n")
