import requests
import pandas as pd
from io import StringIO

url = "https://www.datos.gov.co/resource/s54a-sgyg.csv"

parametros = {
    "$where": "departamento='ATLANTICO' AND municipio='BARRANQUILLA'",
    "$limit": 50000
}

respuesta = requests.get(url, params=parametros)

respuesta.raise_for_status()

df = pd.read_csv(StringIO(respuesta.text))

print("Registros encontrados:", len(df))
print(df.head())

df.to_csv(
    "../dataset/precipitacion_barranquilla.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Archivo guardado correctamente.")