# Importamos la libreria requests
# para consultar informacion de internet
import requests

# Direccion de la API
URL = "https://api.open-meteo.com/v1/forecast"

# Configuramos la ubicacion 
# current -> indica que queremos consultar los datos actuales
# temperature_2m -> temperatura actual a 2 metros de altura
# wind_speed_10m -> velocidad del viento a 10 metros de altura
params = {
    "latitude": 2.4419,
    "longitude": -76.6063,
    "current": "temperature_2m,wind_speed_10m",
}

# Realizamos la peticion a la pagina y guardamos la respuesta que devuelve
r = requests.get(URL, params=params)

# Se convierte la respuesta de la api en un archivo json
datos = r.json()

# Obtenemos la informacion
actual = datos["current"]

# Mostramos los resultados
print("Temperatura:", actual["temperature_2m"], "°C")
print("Viento:", actual["wind_speed_10m"], "km/h")

