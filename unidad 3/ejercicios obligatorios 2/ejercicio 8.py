# Cargar dos arrays de 5 elementos cada uno
# Comparar si ambos son iguales elemento a elemento
# Mostrar un mensaje indicando si son o no iguales.

array_a = [1, 2, 3, 4, 5]
array_b = [2, 1, 3, 6, 5]

for i in range(5):
    if array_a[i] == array_b[i]:
        print(f"{array_a[i]} y {array_b[i]} son iguales!! :)")
    else:
        print(f"{array_a[i]} y {array_b[i]} no son iguales!! :(") 