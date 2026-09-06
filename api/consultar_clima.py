import requests

# URL de la API de Open-Meteo
url = "https://api.open-meteo.com/v1/forecast"

# Coordenadas aproximadas de Barranquilla
parametros = {
    "latitude": 10.9685,
    "longitude": -74.7813,
    "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
    "timezone": "America/Bogota"
}

# Hacer la petición a la API
respuesta = requests.get(url, params=parametros)

# Verificar si la petición fue exitosa
respuesta.raise_for_status()

# Convertir la respuesta JSON
datos = respuesta.json()

# Mostrar los datos
print("Datos obtenidos de Open-Meteo:")
print(datos)