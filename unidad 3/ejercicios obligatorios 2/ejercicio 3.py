# Declarar un array de 6 números reales (floats)
# Cargarlo por teclado
# Calcular y mostrar el promedio de los valores

numeros = [0] * 6
suma_numeros = 0
promedio = 0

print("Ingrese 6 números enteros para realizar el promedio: ")
for i in range(6):
    numeros[i] = float(input(f"Número {i+1}: "))
    suma_numeros += numeros[i]

promedio = suma_numeros / len(numeros)

print(f"Su promedio es de {promedio}")
