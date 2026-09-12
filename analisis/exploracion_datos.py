import pandas as pd

RUTA_ACCIDENTES = "dataset/Accidentalidad_en_Barranquilla_20260830.csv"
RUTA_PRECIPITACION = "dataset/precipitacion_barranquilla.csv"

# Cargar los datasets
df_accidentes = pd.read_csv(RUTA_ACCIDENTES)
df_precipitacion = pd.read_csv(RUTA_PRECIPITACION)

# Dimensiones
print("ACCIDENTES")
print("Dimensiones:", df_accidentes.shape)

print("\nPRECIPITACIÓN")
print("Dimensiones:", df_precipitacion.shape)

# Tipos de datos
print("\nTIPOS DE DATOS")

for nombre, df in [
    ("ACCIDENTES", df_accidentes),
    ("PRECIPITACIÓN", df_precipitacion)
]:
    print(f"\n{nombre}:")
    print(dict(df.dtypes.astype(str)))