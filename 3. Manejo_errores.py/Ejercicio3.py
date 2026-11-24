# Se define una funcion para dividir de forma segura
def dividir_seguro(a, b):
    try:
        # Intenta dividir el primer numero entre el segundo
        return a / b

    except ZeroDivisionError:
        # Muestra un error si el divisor es 0 y se evita que el programa falle
        print("No se puede dividir entre cero")
        return None 

# Probamos que funcione bien dividiendo engtre 2 y 0
print("El resultado es: ", dividir_seguro(10, 2))
print("El resultado es: ", dividir_seguro(5, 0))