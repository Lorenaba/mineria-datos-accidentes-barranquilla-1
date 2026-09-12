# Minería de Datos - Accidentes de Tránsito en Barranquilla

## Descripción del proyecto

Este proyecto tiene como objetivo realizar un análisis mediante técnicas de minería de datos sobre los accidentes de tránsito registrados en la ciudad de Barranquilla.

## Conjunto de datos

El conjunto de datos contiene información sobre accidentes de tránsito registrados en Barranquilla. Entre los datos disponibles se encuentran la fecha, hora, gravedad, clase de accidente, sitio donde ocurrió y cantidad de heridos y fallecidos.

### Principales variables

* Fecha del accidente
* Hora del accidente
* Gravedad del accidente
* Clase de accidente
* Sitio exacto del accidente
* Cantidad de heridos
* Cantidad de muertos
* Año
* Mes
* Día

## ¿Qué se puede hacer con estos datos?

Los datos permiten analizar diferentes patrones relacionados con los accidentes de tránsito, como los días, meses y horarios en los que ocurren con mayor frecuencia y los tipos de accidentes más comunes.

También se podría utilizar la información histórica para intentar predecir la gravedad de un accidente según sus características.

## Fuentes de datos

Para el desarrollo del proyecto se definieron dos conjuntos de datos principales y una API complementaria. Los dos datasets permiten analizar la relación entre los accidentes de tránsito y las condiciones de precipitación registradas en Barranquilla.

### Fuente 1. Accidentalidad en Barranquilla

* **Nombre:** Accidentalidad en Barranquilla
* **Fuente:** Datos Abiertos Colombia
* **Formato:** CSV
* **Número de filas:** 28.523
* **Número de columnas:** 11
* **Variables principales:** `FECHA_ACCIDENTE`, `HORA_ACCIDENTE`, `GRAVEDAD_ACCIDENTE`, `CLASE_ACCIDENTE`, `SITIO_EXACTO_ACCIDENTE`, `CANT_HERIDOS_EN_SITIO_ACCIDENTE`, `CANT_MUERTOS_EN_SITIO_ACCIDENTE`, `CANTIDAD_ACCIDENTES`, `AÑO_ACCIDENTE`, `MES_ACCIDENTE` y `DIA_ACCIDENTE`.
* **Posible variable objetivo:** `GRAVEDAD_ACCIDENTE`.

Este conjunto contiene registros de accidentes de tránsito ocurridos en Barranquilla, incluyendo información temporal, ubicación, gravedad y cantidad de heridos y muertos.

### Fuente 2. Precipitación en Barranquilla

* **Nombre:** Precipitación
* **Fuente:** IDEAM - Datos Abiertos Colombia
* **Formato:** CSV
* **Municipio:** Barranquilla
* **Variables principales:** `codigoestacion`, `codigosensor`, `fechaobservacion`, `valorobservado`, `nombreestacion`, `departamento`, `municipio`, `latitud`, `longitud`, `descripcionsensor` y `unidadmedida`.
* **Variable principal:** `valorobservado`, que representa la precipitación registrada en milímetros (mm).

Este conjunto contiene mediciones reales realizadas por estaciones meteorológicas ubicadas en Barranquilla. Los registros incluyen la fecha y hora de observación, la cantidad de precipitación y la ubicación de la estación.

### Fuente 3. API complementaria: Open-Meteo

* **Nombre:** Open-Meteo
* **Tipo:** API REST
* **Formato de respuesta:** JSON
* **Categoría:** Clima
* **Uso en el proyecto:** complementar la información meteorológica obtenida de los datasets y realizar consultas de variables como temperatura, humedad, precipitación y velocidad del viento.

## Relación entre los datasets

Los dos datasets principales pueden relacionarse principalmente mediante la **fecha y hora**.

El dataset de accidentalidad registra la fecha y hora en que ocurrió cada accidente, mientras que el dataset de precipitación registra la fecha y hora en que una estación meteorológica realizó una medición de lluvia.

Esta relación permitirá analizar si existe una asociación entre la **precipitación y la ocurrencia de accidentes de tránsito en Barranquilla**.

Una posible pregunta de análisis es:

**¿Cuando llueve, ocurren más accidentes de tránsito en Barranquilla?**

La API de Open-Meteo se utilizará como fuente complementaria de información meteorológica y no como uno de los dos datasets principales del análisis.

**Comparación de tipos de datos**

Al cargar los dos datasets con Pandas, se identificaron los siguientes tipos de datos:

| ACCIDENTES                         | Tipo      | PRECIPITACIÓN       | Tipo      |
| ---------------------------------- | --------- | ------------------- | --------- |
| `FECHA_ACCIDENTE`                  | `object`  | `codigoestacion`    | `int64`   |
| `HORA_ACCIDENTE`                   | `object`  | `codigosensor`      | `int64`   |
| `GRAVEDAD_ACCIDENTE`               | `object`  | `fechaobservacion`  | `object`  |
| `CLASE_ACCIDENTE`                  | `object`  | `valorobservado`    | `float64` |
| `SITIO_EXACTO_ACCIDENTE`           | `object`  | `nombreestacion`    | `object`  |
| `CANT_HERIDOS_EN _SITIO_ACCIDENTE` | `float64` | `departamento`      | `object`  |
| `CANT_MUERTOS_EN _SITIO_ACCIDENTE` | `float64` | `municipio`         | `object`  |
| `CANTIDAD_ACCIDENTES`              | `int64`   | `zonahidrografica`  | `object`  |
| `AÑO_ACCIDENTE`                    | `int64`   | `latitud`           | `float64` |
| `MES_ACCIDENTE`                    | `object`  | `longitud`          | `float64` |
| `DIA_ACCIDENTE`                    | `object`  | `descripcionsensor` | `object`  |
| —                                  | —         | `unidadmedida`      | `object`  |

## Diagnóstico y calidad de los datos

Se realizó un diagnóstico inicial de los dos conjuntos de datos utilizando Python y Pandas.

El dataset de accidentes contiene **28.523 registros y 11 variables**, mientras que el dataset de precipitación contiene **50.000 registros**.

En el dataset de accidentes se identificaron inicialmente:

* **15.693 valores faltantes** en la cantidad de heridos.
* **28.186 valores faltantes** en la cantidad de muertos.
* **0 registros duplicados**.

En el dataset de precipitación no se encontraron valores faltantes ni registros duplicados.

Los principales problemas identificados fueron los valores faltantes, la necesidad de convertir las variables de fecha y hora a un formato temporal, la presencia de posibles valores extremos en la cantidad de heridos y la distribución de la precipitación, donde la mayoría de las mediciones presentan valores de **0 mm**.

## Tratamiento de valores faltantes

Para tratar los valores faltantes se utilizó `GRAVEDAD_ACCIDENTE` como información auxiliar, ya que permite interpretar el significado de algunos datos faltantes.

En los accidentes clasificados como **`Solo daños`**, se asignó el valor **0** a heridos y muertos, debido a que esta categoría indica que no hubo personas lesionadas ni fallecidas.

En los registros clasificados como **`Con heridos`**, se asignó **0** a la cantidad de muertos, debido a que la categoría indica que hubo personas heridas pero no fallecidas.

En los registros clasificados como **`Con muertos`**, permanecieron **223 valores faltantes** en la cantidad de heridos. Estos valores no fueron reemplazados porque no existe información suficiente para determinar la cantidad real de personas heridas.

El patrón de valores faltantes no se considera completamente aleatorio (MCAR), debido a que presenta relación con una variable observada como `GRAVEDAD_ACCIDENTE`. El análisis es compatible con un mecanismo relacionado con variables observadas, aunque no se afirma de manera definitiva que corresponda a MAR o MNAR únicamente con la información disponible.

## Tratamiento de valores extremos mediante IQR

Se utilizó el **rango intercuartílico (IQR)** para identificar posibles valores extremos en las variables numéricas.

Para la cantidad de heridos se obtuvo:

* Q1 = 0
* Q3 = 1
* IQR = 1
* Límite superior = 2,5

Los valores superiores a 2,5 fueron identificados como posibles valores extremos. Sin embargo, no fueron eliminados porque representan cantidades de heridos que pueden ser reales en accidentes de mayor gravedad.

En el caso de la precipitación, el IQR presentó un límite superior igual a **0 mm**, debido a que la mayoría de las mediciones corresponden a ausencia de lluvia. Los valores superiores a 0 mm fueron conservados porque representan mediciones reales de precipitación necesarias para el análisis.

## Conversión y validación de fechas

Las variables de fecha y hora fueron convertidas a formato temporal mediante `pd.to_datetime()`.

La fecha y hora de los accidentes fueron combinadas en una nueva variable denominada `FECHA_HORA_ACCIDENTE`.

En la validación no se encontraron fechas ni horas inválidas.

Las mediciones de precipitación también fueron convertidas a formato de fecha y hora mediante la variable `fechaobservacion`.

## Integración de accidentes y precipitación

Para analizar la relación entre accidentes y lluvia se identificó el período común disponible entre ambos datasets.

Posteriormente, los accidentes fueron relacionados con la medición de precipitación temporalmente más cercana.

Para evitar asociaciones poco confiables, solamente se conservaron coincidencias con una diferencia máxima de **10 minutos**.

Como resultado se obtuvieron **6.955 coincidencias válidas**.

De estas coincidencias:

* **66 accidentes** ocurrieron durante una medición con lluvia.
* **6.889 accidentes** ocurrieron durante una medición sin lluvia.

Se creó la variable `CON_LLUVIA`, considerando como condición de lluvia aquellos registros cuyo valor de precipitación fue mayor que **0 mm**.

## Resultados preliminares

Como análisis descriptivo inicial se calculó una tasa de accidentes por cada 100 mediciones.

| Condición  | Accidentes por cada 100 mediciones |
| ---------- | ---------------------------------: |
| Con lluvia |                              11,56 |
| Sin lluvia |                              13,94 |

La tasa calculada fue aproximadamente **17,07 % menor durante las mediciones con lluvia**.

Este resultado es únicamente descriptivo y preliminar. No permite afirmar que la lluvia reduzca los accidentes, debido a las diferencias en la cobertura temporal de los datasets y a las limitaciones de las mediciones disponibles.

## Validación final

Después del proceso de limpieza se realizó una validación de los resultados.

El dataset de accidentes conserva sus **28.523 registros originales**, no presenta duplicados y mantiene únicamente **223 valores faltantes** en la cantidad de heridos, los cuales fueron conservados de manera intencional por falta de información suficiente.

El dataset de precipitación conserva sus **50.000 registros**, sin duplicados ni valores faltantes.

También se revisaron los rangos numéricos y no se encontraron valores negativos en las cantidades de heridos, muertos o precipitación.

El análisis integrado contiene **6.955 coincidencias válidas**, todas con una diferencia temporal máxima de 10 minutos.

## Archivos generados

Como resultado del proceso de limpieza se generaron los siguientes archivos:

```text
dataset/Accidentalidad_en_Barranquilla_limpio.csv
dataset/precipitacion_barranquilla_limpio.csv
analisis/limpieza_datos.ipynb
```

El notebook contiene el proceso de diagnóstico, limpieza, tratamiento de valores faltantes, detección de valores extremos, integración de los datasets y validación final.

## Conclusión

El proyecto permitió realizar un proceso de limpieza y preparación de datos de accidentalidad y precipitación en Barranquilla.

El análisis preliminar encontró una tasa menor de accidentes durante las mediciones con lluvia en comparación con las mediciones sin lluvia. Sin embargo, este resultado no permite establecer una relación causal ni afirmar que la lluvia disminuya los accidentes.

Los datasets quedan preparados para continuar con análisis estadísticos y técnicas de minería de datos que permitan estudiar con mayor profundidad la relación entre las condiciones climáticas y la accidentalidad.
