# Función principal del programa  
def main():  
    # Leer dos números por teclado  
    num1 = float(input("Introduce el primer número: "))  
    num2 = float(input("Introduce el segundo número: "))  

    # Mostrar menú de opciones  
    print("Seleccione una opción:")  
    print("1: Sumar los dos números")  
    print("2: Restar el segundo número del primero")  
    print("3: Multiplicar los dos números")  

    # Leer opción del usuario  
    opcion = input("Ingrese su opción (1, 2 o 3): ")  

    # Realizar la opción seleccionada  
    if opcion == "1":  
        resultado = num1 + num2  
        print(f"La suma es: {resultado}")  
    elif opcion == "2":  
        resultado = num1 - num2  
        print(f"La resta es: {resultado}")  
    elif opcion == "3":  
        resultado = num1 * num2  
        print(f"La multiplicación es: {resultado}")  
    else:  
        print("Opción no válida. Por favor elige 1, 2 o 3.")  

# Ejecutar el programa  
if __name__ == "__main__":  
    main()