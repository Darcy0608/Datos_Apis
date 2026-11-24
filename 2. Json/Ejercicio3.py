import json

with open("inventario.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

# Agregamos bufanda a la lista
datos.append({
    "producto": "Bufanda",
    "precio": 25000,
    "stock": 15
})

with open("inventario.json", "w", encoding="utf-8") as f:
    # Guardamos de nuevo todos los productos, incluyendo la bufanda
    json.dump(datos, f, indent=4, ensure_ascii=False)

# Contamos cuantos productos hay en la lista
print("Cantidad de productos:", len(datos))