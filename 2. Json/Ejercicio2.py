import json

# Abrimos el archivo para leerlo
with open("inventario.json", "r", encoding="utf-8") as f:
    # Guardamos la info que acabamos de leer
    datos = json.load(f)

for producto in datos:
    # Comprobamos si el stock es menos que 10
    if producto["stock"] < 10:
        # Muestra el nombre de el producto que cumple esa condicion
        print(producto["producto"])