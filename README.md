Minería de Datos - Accidentes de Tránsito en Barranquilla Descripción del proyecto

Este proyecto tiene como objetivo realizar un análisis mediante técnicas de minería de datos sobre los accidentes de tránsito registrados en la ciudad de Barranquilla.

Conjunto de datos

El conjunto de datos contiene información sobre accidentes de tránsito registrados en Barranquilla. Entre los datos disponibles se encuentran la fecha, hora, gravedad, clase de accidente, sitio donde ocurrió y cantidad de heridos y fallecidos.

Principales variables Fecha del accidente Hora del accidente Gravedad del accidente Clase de accidente Sitio exacto del accidente Cantidad de heridos Cantidad de muertos Año Mes Día ¿Qué se puede hacer con estos datos?

Los datos permiten analizar diferentes patrones relacionados con los accidentes de tránsito, como los días, meses y horarios en los que ocurren con mayor frecuencia y los tipos de accidentes más comunes.

También se podría utilizar la información histórica para intentar predecir la gravedad de un accidente según sus características.

Conjunto de datos utilizado

El conjunto de datos utilizado en este proyecto fue obtenido del portal de Datos Abiertos Colombia.

1. API externa

Para complementar el dataset de accidentes de tránsito se utilizará
la API de clima histórico de Open-Meteo.

Esta API proporciona información meteorológica histórica como
temperatura, precipitación, humedad y velocidad del viento.

Los datos obtenidos mediante la API se podrán relacionar con el dataset
de accidentalidad utilizando la fecha y hora del accidente.

El propósito de esta integración es analizar si las condiciones
climáticas pueden estar relacionadas con la frecuencia o gravedad
de los accidentes de tránsito en Barranquilla.
