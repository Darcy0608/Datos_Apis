# Importamos la libreria requests 
import requests

URL = "https://api.open-meteo.com/v1/forecast"

# Creamos la funcion
def consultar_clima(lat, lon):
    # Creamos los parametros. 
    # Este es un diccionario, permite almacenar info -> Clave - Valor
    params = {
        "latitude": lat,    
        "longitude": lon,   
        "current": "temperature_2m,wind_speed_10m",
    }

    # Utiliamos try para intentar ejecutar las instrucciones que estan en ese bloque
    try:
        # Realizamos la peticion
        r = requests.get(URL, params=params, timeout=10)
        # Se comprueba si la respuesta del servidor tiene un error
        r.raise_for_status()

        return r.json()

    except requests.exceptions.RequestException:
        print("No se pudo consultar el clima")
        return None

# Se ejecuta la funcion, se le envian las coordenadas de popayan
datos = consultar_clima(2.4419, -76.6063)

# Se comprueba el resultado
if datos is not None:
    actual = datos["current"]
    print("Temperatura:", actual["temperature_2m"], "°C")
    print("Viento:", actual["wind_speed_10m"], "km/h")
