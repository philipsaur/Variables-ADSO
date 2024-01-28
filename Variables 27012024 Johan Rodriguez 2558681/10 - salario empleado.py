print("PROGRAMA PARA CALCULAR EL SALARIO DE UN EMPLEADO SEGUN SUS DIAS DE TRABAJO\n")

salario_diario = float(input("Ingresa el salario diario del empleado:"))
dias_trabajados = int(input("Ingresa el número de días trabajados:"))

salario = salario_diario * dias_trabajados

pension = 0.10 * salario
salud = 0.15 * salario

salario_completo = salario - pension - salud

print(f"\nEl salario a pagar al empleado es {salario_completo}\n")
