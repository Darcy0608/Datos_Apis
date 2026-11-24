# Creamos un bucle, se repete hasta que el usuario ingrese un numero que sea valido
while True:
    try:
        # Pide el valor y lo convierte en decimal 
        numero = float(input("Ingresa un número: "))
        break
    except ValueError:
        # Si se ingresa letras o simbolos sale un aviso y se repite
        print("Eso no es un número. Inténtalo nuevamente.")

# Se muestra el resultado en consola del numero guardado
print("Número recibido:", numero)