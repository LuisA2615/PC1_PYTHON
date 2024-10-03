# Solicitar al usuario que ingrese una hora en formato de 24 horas  
hora_input = input("Ingrese una hora (formato 24 horas, ej. 07:30): ")  

# Convertir la entrada de hora a una lista de enteros [hora, minutos]  
hora, minutos = map(int, hora_input.split(":"))  

# Función para determinar la hora de la comida  
def determinar_hora_comida(hora, minutos):  
    if (hora == 7 and 0 <= minutos <= 59) or (hora == 8 and minutos == 0):  
        print("Es hora del desayuno.")  
    elif (hora == 12 and 0 <= minutos <= 59) or (hora == 13 and minutos == 0):  
        print("Es hora del almuerzo.")  
    elif (hora == 18 and 0 <= minutos <= 59) or (hora == 19 and minutos == 0):  
        print("Es hora de la cena.")  
    else:  
        print("No es hora de comer.")  

# Llamar a la función con los valores ingresados  
determinar_hora_comida(hora, minutos)