# Escribir una función que reciba un array de enteros y un número a buscar
# La función debe retornar la posición de la primera aparición de ese número o -1 si no se encuentra

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def encontrar(primos, numero_inp):
    for i in range(len(primos)):
        if primos[i] == numero_inp:
            return i
    return -1

print("Bienvenido a Detecté-un-Primo-3000.com !")
numero_inp = int(input("Ingrese un número del 1 al 50 y fijese si es primo: "))

posición = encontrar(primos, numero_inp)

if posición != -1:
    print(f"Es primo!! se encuentra en el puesto {posición}")
else:
    print(f"Ese número no es primo :( , se encuentra en la posición {posición}")