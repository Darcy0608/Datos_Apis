try:
    # Intenta abrir y leer el archivo de text
    with open("no_existe.txt", "r", encoding="utf-8") as f:
        contenido = f.read()
        print(contenido)

except FileNotFoundError:
    # Se muestra un aviso si el archivo no se encuentra
    print("El archivo no existe. Revisa el nombre o la carpeta.")