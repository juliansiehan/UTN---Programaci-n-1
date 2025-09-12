# Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero

numeros = [11, 12, 13, 14, 15, 16]
x = len(numeros)

for x in range(6):  
    print(numeros[x])
    x -= 1
