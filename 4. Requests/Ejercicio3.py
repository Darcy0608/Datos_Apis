import requests
import json

URL = "https://api.open-meteo.com/v1/forecast"

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


datos = consultar_clima(2.4419, -76.6063)

# Se comprueba que existan datos 
if datos is not None:

    # Se guarda la respuesta
    with open("clima.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    # Se lee el archivo
    with open("clima.json", "r", encoding="utf-8") as f:
        clima = json.load(f)

    # Obtenemos la temperatura
    actual = clima["current"]

    print("Temperatura:", actual["temperature_2m"], "°C")