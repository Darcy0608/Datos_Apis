# Importamos la libreria json -
import json

class CarritoCompras:

    def __init__(self):
        # Inicializamos una lista vacia para guardar los productos
        self.productos = []

    def agregar_producto(self, nombre, precio):
        # Guardamos cada producto como un diccionario
        self.productos.append({"nombre": nombre, "precio": precio})

    def total(self):
        suma = 0

        for p in self.productos:
            suma += p["precio"]

        return suma

    # Agregamos el metodo guardar - 
    def guardar(self, archivo):
        # Guardamos los productos en un archivo JSON
        with open(archivo, "w", encoding="utf-8") as f:
            # self.productos -> contiene los productos del carrito. json.dump() -> guarda esa lista en formato JSON
            json.dump(self.productos, f, indent=4, ensure_ascii=False)
    
    # Agregamos el metodo cargar(archivo) -
    def cargar(self, archivo):
        # Leemos los productos que estan guardados en el JSON
        with open(archivo, "r", encoding="utf-8") as f:
            self.productos = json.load(f)


# Creamos el primer carrito
carrito1 = CarritoCompras()

carrito1.agregar_producto("Laptop", 2500000)
carrito1.agregar_producto("Mouse", 50000)
carrito1.agregar_producto("Teclado", 90000)

# Guardamos el primer carrito
carrito1.guardar("carrito.json")

# Creamos un segundo carrito vacio
carrito2 = CarritoCompras()

# Cargamos los productos del archivo en el segundo carrito
carrito2.cargar("carrito.json")

# Mostramos los productos y el total del segundo carrito
print("Productos del segundo carrito:")
print(carrito2.productos)

print("Total a pagar:", carrito2.total())
