# Clasificación de Flores dataset Iris
Oscar David Barbosa Rodríguez


Introducción a Machine Learning 801


Link de repositorio: https://github.com/ODavidBRodriguez/Clasificacion-dataset-IRIS.git

Este proyecto tiene como objetivo demostrar un método de clasificación de aprendizaje automático utilizando el popular dataset de flores Iris. Para ello, se ha implementado un modelo de **Regresión Lineal** con la técnica de clasificación multiclase **"One-vs-Rest"**.

## 1. Fundamentos del Proyecto

El dataset de Iris contiene 150 muestras de flores, cada una con 4 características (`largo_sepalo`, `ancho_sepalo`, `largo_petalo`, `ancho_petalo`) y una de las tres posibles especies (`Setosa`, `Versicolor`, `Virginica`).

El enfoque "One-vs-Rest" consiste en entrenar tres modelos de regresión lineal separados:
* Un modelo para predecir si una flor es **Setosa** o no lo es.
* Un modelo para predecir si una flor es **Versicolor** o no lo es.
* Un modelo para predecir si una flor es **Virginica** o no lo es.

La clase predicha final para una nueva flor es aquella cuyo modelo arrojó la puntuación más alta.

## 2. Ecuaciones de los Modelos

Cada modelo de regresión lineal se basa en una ecuación que asigna un peso (coeficiente) a cada característica y un valor de inicio (intercepto). 

Las ecuaciones calculadas para cada uno de los tres modelos son:

* Modelo para la clase 'Setosa'

  y = 0.1319 + 0.0459 * largo_sepalo + 0.2624 * ancho_sepalo - 0.2141 * largo_petalo - 0.0595 * ancho_petalo

* Modelo para la clase 'Versicolor'

  y = 1.4837 + 0.0246 * largo_sepalo - 0.4650 * ancho_sepalo + 0.1734 * largo_petalo - 0.4285 * ancho_petalo

* Modelo para la clase 'Virginica'

  y = -0.6156 - 0.0704 * largo_sepalo + 0.2026 * ancho_sepalo + 0.0408 * largo_petalo + 0.4880 * ancho_petalo

## 3. Resultados y Métricas
El modelo fue entrenado en el 80% de los datos y evaluado en el 20% restante. Además, el modelo alcanzó una precisión general del 87%.

La precisión varía según la clase. Este gráfico de barras muestra la tasa de predicciones correctas para cada especie.
![Gráfico de barras Precisión por clase](imgs/precision_por_clase.png)

Este gráfico de barras desglosa la importancia de cada característica para la clasificación de cada clase, basándose en la magnitud de los coeficientes de la regresión lineal.
![Gráfico de barras Precisión por clase](imgs/importancia_caracteristicas.png)

## 4. Exportación de Resultados
Todos los resultados de la clasificación se exportan automáticamente a un archivo de Excel (clasificacion_iris.xlsx) en la carpeta resultados/ para un análisis más detallado. El script sobrescribe el archivo si ya existe, garantizando que los datos estén siempre actualizados.

El archivo de Excel contiene los resultados de las clasificacion para los datos tomados como prueba (30 en total) en el cual se pueden apreciar las características de cada flor de prueba, su clase o tipo de flor real y su clase predicha. Al final hay una columna la cual indica si la predicción fue correcta en base a la clase real y la predicha, esto con el fin de poder visualizar los resultados de las predicciones y la precisión del modelo.

El archivo puede ser visualizado en la carpeta resultados/. La siguiente imágen en una captura de pantalla del archivo excel y algunos de los resultados obtenidos de la predicción.
