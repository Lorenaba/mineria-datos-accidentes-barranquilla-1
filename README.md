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

Para el desarrollo del proyecto se definieron dos fuentes de datos relacionadas con la accidentalidad vial en Barranquilla. La primera fuente corresponde al dataset principal de accidentalidad y la segunda es una API externa de información meteorológica.

### Fuente 1. Accidentalidad en Barranquilla

* **Nombre:** Accidentalidad en Barranquilla
* **Fuente:** Datos Abiertos Colombia
* **Formato:** CSV
* **Número de filas:** 28.523
* **Número de columnas:** 11
* **Variables principales:** `FECHA_ACCIDENTE`, `HORA_ACCIDENTE`, `GRAVEDAD_ACCIDENTE`, `CLASE_ACCIDENTE`, `SITIO_EXACTO_ACCIDENTE`, `CANT_HERIDOS_EN_SITIO_ACCIDENTE`, `CANT_MUERTOS_EN_SITIO_ACCIDENTE`, `CANTIDAD_ACCIDENTES`, `AÑO_ACCIDENTE`, `MES_ACCIDENTE` y `DIA_ACCIDENTE`.
* **Posible variable objetivo:** `GRAVEDAD_ACCIDENTE`.

Este conjunto de datos contiene registros de accidentes de tránsito ocurridos en Barranquilla, incluyendo información temporal, ubicación del accidente, gravedad y cantidad de heridos y muertos.

### Fuente 2. Open-Meteo

* **Nombre:** Open-Meteo
* **Tipo:** API REST
* **Formato de respuesta:** JSON
* **Categoría:** Weather
* **Variables disponibles:** temperatura, humedad relativa, precipitación y velocidad del viento.
* **Uso en el proyecto:** complementar la información de accidentalidad con variables meteorológicas para analizar una posible relación entre las condiciones climáticas y los accidentes de tránsito.

## Relación entre las fuentes

Las dos fuentes se pueden relacionar principalmente mediante las variables de **fecha y hora**.

El dataset de accidentalidad contiene la fecha y hora en que ocurrió cada accidente, mientras que Open-Meteo permite obtener información meteorológica para una fecha, hora y ubicación determinadas.

El objetivo es utilizar la información climática como fuente complementaria para estudiar si las condiciones meteorológicas pueden estar relacionadas con la gravedad o comportamiento de los accidentes registrados en Barranquilla.
