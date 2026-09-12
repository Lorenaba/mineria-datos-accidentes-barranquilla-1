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
* **Categoría:** Weather
* **Uso en el proyecto:** complementar la información meteorológica obtenida de los datasets y realizar consultas de variables como temperatura, humedad, precipitación y velocidad del viento.

## Relación entre los datasets

Los dos datasets principales pueden relacionarse principalmente mediante la **fecha y hora**.

El dataset de accidentalidad registra la fecha y hora en que ocurrió cada accidente, mientras que el dataset de precipitación registra la fecha y hora en que una estación meteorológica realizó una medición de lluvia.

Esta relación permitirá analizar si existe una asociación entre la **precipitación y la ocurrencia de accidentes de tránsito en Barranquilla**.

Una posible pregunta de análisis es:

**¿Cuando llueve, ocurren más accidentes de tránsito en Barranquilla?**

La API de Open-Meteo se utilizará como fuente complementaria de información meteorológica y no como uno de los dos datasets principales del análisis.
