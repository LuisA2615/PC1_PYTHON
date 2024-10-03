def obtener_tipo_mime(nombre_archivo):  
    # Diccionario de extensiones y sus tipos MIME  
    tipos_mime = {  
        '.gif': 'image/gif',  
        '.jpg': 'image/jpeg',  
        '.jpeg': 'image/jpeg',  
        '.png': 'image/png',  
        '.pdf': 'application/pdf',  
        '.txt': 'text/plain',  
        '.zip': 'application/zip'  
    }  
    
    # Convertir el nombre del archivo a minúsculas  
    nombre_archivo = nombre_archivo.lower()  
    
    # Verificar la extensión  
    for sufijo, tipo in tipos_mime.items():  
        if nombre_archivo.endswith(sufijo):  
            return tipo  
    
    # Si no coincide con ninguna extensión conocida  
    return 'application/octet-stream'  

# Solicitar al usuario el nombre del archivo  
nombre_archivo = input("Introduce el nombre del archivo: ")  
tipo_mime = obtener_tipo_mime(nombre_archivo)  

# Mostrar el tipo MIME correspondiente  
print(f"El tipo MIME para '{nombre_archivo}' es: {tipo_mime}")