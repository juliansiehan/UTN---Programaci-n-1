# Declarar un array de 10 enteros.
# Cargarlo por teclado
# Calcular y mostrar la suma de todos los elementos.

numeros = [0] * 10
suma = 0

print("Ingrese 10 números enteros para realizar la suma: ")
for i in range(10):
    numeros[i] = int(input(f"Número {i+1}: "))

# Cuando en la cosigna dice "mostrar la suma" se refiere a lo de abajo?
# O es solo quiere que se vea el resultado?

print("Ok, perfecto! Con los datos dados, podemos hacer la suma:") 
for i in range(10):
    print(f"{suma} + {numeros[i]} =")
    suma += numeros[i]
    print(f"{suma}")

print(f"El resultado es {suma}!")