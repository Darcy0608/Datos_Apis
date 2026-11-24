import requests
import json

URL = "https://api.open-meteo.com/v1/forecast"

# PARTE 1 - Clima de Popayan
# PARTE 2 - Funcion consultar_clima

def consultar_clima(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
    }

    try:
        r = requests.get(URL, params=params, timeout=10)
        r.raise_for_status()
        return r.json()

    except requests.exceptions.RequestException:
        print("No se pudo consultar el clima")
        return None

# Ejecutamos la consulta
datos = consultar_clima(2.4419, -76.6063)

if datos is not None:

    # Parte 1: Mostrar temperatura y viento
    actual = datos["current"]
    print("Temperatura:", actual["temperature_2m"], "°C")
    print("Viento:", actual["wind_speed_10m"], "km/h")

    # Parte 3: Guardar y leer la respuesta
    with open("clima.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

    with open("clima.json", "r", encoding="utf-8") as f:
        clima = json.load(f)

    print("\nTemperatura:", clima["current"]["temperature_2m"], "°C")