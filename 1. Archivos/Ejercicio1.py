# Creamos la lista de estudiantes
estudiantes = ["Carlos", "Ana", "Luis"]


print(" Estudiantes: ")
# Guardar y leer linea por linea
# Guardamos los nombres en un archivo
with open("estudiantes.txt", "w", encoding="utf-8") as f:
    for nombre in estudiantes:
        f.write(nombre + "\n")

# Leemos el archivo
with open("estudiantes.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        print(i, linea.strip())

