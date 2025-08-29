def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))    

operaciones(num1, num2)
    
