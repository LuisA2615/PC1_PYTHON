# Ingresar venta 
payasos=int(input("Ingresar la cantidad de payasos vendidos: "))
muñecas=int(input("Ingresar la cantidad de muñecas vendidas: "))

# Calcular peso de cada producto
peso_payaso= payasos*112
peso_muñecas= muñecas*75
Peso_total= peso_payaso+peso_muñecas

# Salida
print(f"La cantidad de payasos vendidos es: {payasos} unidades")
print(f"La cantidad de muñecas vendidas es: {muñecas} unidades")
print(f"El peso total es: {Peso_total} gramos")


