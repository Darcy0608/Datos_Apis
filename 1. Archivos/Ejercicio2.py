# Usamos "a" y no "w" por que borraria los nombres anteriores
# mientras que "a" los conserva

# Abrimos el archivo txt para agregar la info
with open("estudiantes.txt", "a", encoding="utf-8") as f:
    f.write("Marta\n")

# Comprobar la lista actualizada leyendo de nuevo
print("Lista de estudiantes actualizada: ")
with open("estudiantes.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        print(i, linea.strip())

# Leemos el archivo, mostramos la cantidad
with open("estudiantes.txt", "r", encoding="utf-8") as f:
    estudiantes = f.readlines()

    # Contamos los estudiantes
    cantidad = len(estudiantes)

    print("\n Cantidad de estudiantes:", cantidad)

