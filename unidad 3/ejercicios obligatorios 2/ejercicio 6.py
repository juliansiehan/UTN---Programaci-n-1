# Cargar un array de 7 números enteros
# Determinar el valor más alto y en qué posición se encuentra

# En ningun momento dice que los valores del array deben ser cargado
# por teclado, así que supongo que ya estan definidos?
numeros = [3, 6, 65, 64, 754, 74, -13243]
mayor = 0
posición = 0

for i in range(7):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posición = i+1
    else:
        pass

print(f"Los números que tenenmos a mano son: {numeros}")
print(f"El mayor número es {mayor} y su posición es {posición}")

