# Declarar un array de 5 enteros. 
# Cargarlo por teclado y mostrar su contenido por pantalla usando un ciclo for

numeros = [0] * 5

print("Ingrese 5 números enteros:")
for i in range(len(numeros)):
    numeros[i] = int(input(f"Número {i+1}: "))

print("Perfecto! Sus números elegidos fueron:")
for i in range(5):
    print(numeros[i])

# uso las dos formas de poner el rango para que se entienda que entendí :D