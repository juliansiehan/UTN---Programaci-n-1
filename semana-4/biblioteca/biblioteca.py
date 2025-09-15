import funciones

titulos = [""] * 20
ejemplares = [0] * 20

while True:
    funciones.menu()
    opcion = 0
    opcion = (input("Seleccione una opción de las dadas: "))

    if opcion == 1:
        funciones.cargar_titulo()
    elif opcion == 2:
        funciones.mostrar_cat()
    elif opcion == 3:
        funciones.check_disp()
    elif opcion == 4:
        funciones.agotados()
    elif opcion == 5:
        funciones.cargar_tit_esp()
    elif opcion == 6:
        funciones.actualizar()
    elif opcion == 7:
        print("Gracias por usar el sistema! :D")
        break
    else:
        print(f"Error! Opción {opcion} no válida")

# no se por que carajo no anda este menu me rindo ya intente todo que lo haga deepseek