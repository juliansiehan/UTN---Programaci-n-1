def menu():
    print("---------------------------------")
    print("SISTEMA DE CATALOGO DE BIBLIOTECA")
    print("---------------------------------")
    print("1 - Cargar títulos y ejemplares")
    print("2 - Mostrar catalogo completo")
    print("3 - Consultar disponibilidad")
    print("4 - Listar títulos agotados")
    print("5 - Agregar un nuevo título")
    print("6 - Actualizar ejemplares (prestamo/devolución)")
    print("7 - Salir")
    print("---------------------------------")

def elegir_espacio(titulos, x):
    print("Espacios libres:")
    for i in range(20):
        if titulos[i] == "":
            print(f"{i+1}") 
    x = int(input("Elija donde quiere operar: "))
    if x > 20 or x < 0:
        print("Error.")
    else:
        x -= 1
    return x

def cargar_titulo(titulos, ejemplares):
    for i in range(len(titulos)):
        titulos[i] = str(input(f"Escriba el nombre del libro {i+1}: "))
        ejemplares[i] = int(input("Ahora escriba el número de ejemplares que hay: "))

def mostrar_cat(titulos, ejemplares):
    for i in range(len(titulos)):
        if titulos[i] == "":
            continue
    print(f"{i+1} {titulos[i]} - - > {ejemplares[i]} copias")

def check_disp(titulos, ejemplares):
    libro = str(input("Escriba el nombre del libro a buscar: "))
    for i in range(len(titulos)):
        if libro == titulos[i]:
            print(f"{titulos[i]} - - > {ejemplares[i]} copias")
        else:
            continue

def agotados(titulos, ejemplares):
    for i in range(len(titulos)):
        if ejemplares[i] == 0 and titulos != "":
            print(f"{titulos[i]} se encuentra agotado!")
        else:
            pass

def cargar_tit_esp(titulos, ejemplares):
    x = 0
    elegir_espacio(x)
    titulos[x] = str(input("Escriba el nombre del libro a agregar: "))
    ejemplares[x] = int(input("Indique cuantos ejemplares de este quedan: "))

def actualizar(ejemplares):
    x = -1
    mostrar_cat()
    x += int(input("Elija que titulo va a actualizar: "))
    ejemplares[x] = int(input("Cuantos ejemplares hay actualmente? "))

