# Cargar un array de 8 enteros
# Contar cuántos son mayores al valor 100 e informar el resultado

numeros = [0] * 8
nmrs_100 = 0

print("Ingrese 8 números enteros:")
for i in range(8):
    numeros[i] = int(input(f"Número {i+1}: "))
    if numeros[i] > 100:
        nmrs_100 += 1
    else:
        pass

# El "else" de acá está de más pero queda medio fachero jeje :P

print(f"Perfecto! De los numeros dados, los mayores a 100 son: {nmrs_100}")