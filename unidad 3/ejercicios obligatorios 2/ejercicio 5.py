# Cargar un array de 10 enteros
# Solicitar al usuario un número y verificar si se encuentra en el array
# Informar la posición en caso afirmativo, o indicar que no se encuentra

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
intento = 0
si_acerto = False

print("ATENCIÓN: Te tengo un juego ESPELUZNANTE y PERTURBADOR!!!! >:)")
print("Tenes que adivinar uno de los 10 números que tengo en la mente!!")

intento = int(input("Rapido!! Si le erras, te MORÍS!!!!!!!!: "))

for i in range(10):
    if intento == numeros[i]:
        si_acerto = True
    else:
        pass

if si_acerto == True:
    print("Bien ahí capo!! Le pegasta jajaj :D seguís vivo")
    print("(por ahora...)")
else:
    print("MAL!!!! MAL!!!! MEGA MAL!!!!! SUPER MAL!!!!!!!!")
    # activar(gases_toxicos_que_te_matan)