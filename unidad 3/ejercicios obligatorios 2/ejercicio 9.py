# Cargar un array de 10 enteros
# Reemplazar todos los elementos pares por cero y mostrar el array resultante

numeros = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

for i in range(10):
    if numeros[i] % 2 == 0:
        numeros[i] = 0
    else:
        pass

print(numeros)