# Importamos json, nos permite trabajar con archivos JSON
import json

inventario = [
    {"producto": "Camisa", "precio": 45000, "stock": 20},
    {"producto": "Gorra", "precio": 30000, "stock": 5},
    {"producto": "Pantalón", "precio": 89000, "stock": 12},
    {"producto": "Medias", "precio": 8000, "stock": 40},
    {"producto": "Zapatos", "precio": 150000, "stock": 3},
]

with open("inventario.json", "w", encoding="utf-8") as f:
    json.dump(inventario, f, indent=4, ensure_ascii=False)