print("PROGRAMA QUE PERMITE PASAR DE SEGUNDOS A MINUTOS Y HORAS\n")

tiempo_segundos = int(input("Ingresa el tiempo en segundos: "))

horas = tiempo_segundos // 3600  # 1 hora = 3600 segundos
minutos = (tiempo_segundos % 3600) // 60  # 1 minuto = 60 segundos

print(f"\n{tiempo_segundos} segundos es igual a {horas} horas y {minutos} minutos\n")
