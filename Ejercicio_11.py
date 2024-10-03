def eliminar_duplicados(lista):  
    return list(set(lista))  

lista_original = [1, 1, 2, 3, 4, 4, 5, 1]  
lista_procesada = eliminar_duplicados(lista_original)  
print(lista_procesada)