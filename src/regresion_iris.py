import numpy as np
import pandas as pd
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def cargar_y_dividir_datos():
    # Carga el dataset Iris y lo divide en conjuntos de entrenamiento y prueba.
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def entrenar_modelos(X_train, y_train):
    # Entrena un modelo de regresión lineal para cada clase.
    modelos = {}
    clases = np.unique(y_train)
    for clase in clases:
        y_train_binary = (y_train == clase).astype(int)
        modelo = LinearRegression()
        modelo.fit(X_train, y_train_binary)
        modelos[clase] = modelo
    return modelos

def predecir(X, modelos):
    # Predice la clase para un conjunto de datos X.
    y_pred = []
    for X_point in X:
        puntajes = {clase: modelo.predict([X_point])[0] for clase, modelo in modelos.items()}
        clase_pred = max(puntajes, key=puntajes.get)
        y_pred.append(clase_pred)
    return np.array(y_pred)

def generar_resultados(X_test, y_test, y_pred, nombres_clases_es):
    # Genera un DataFrame con los resultados de la clasificación.
    resultados = []
    for i in range(len(X_test)):
        caracteristicas = X_test[i]
        clase_real_idx = y_test[i]
        clase_pred_idx = y_pred[i]
        
        nombre_real = nombres_clases_es[clase_real_idx]
        nombre_predicho = nombres_clases_es[clase_pred_idx]
        resultado_str = "Correcto " if clase_real_idx == clase_pred_idx else "Incorrecto "
        
        resultados.append({
            'Largo_sepalo': caracteristicas[0],
            'Ancho_sepalo': caracteristicas[1],
            'Largo_petalo': caracteristicas[2],
            'Ancho_petalo': caracteristicas[3],
            'Clase_Real': nombre_real,
            'Clase_Predicha': nombre_predicho,
            'Resultado': resultado_str
        })
    return pd.DataFrame(resultados)

def mostrar_ecuaciones(modelos, nombres_features_es, nombres_clases_es):
    """Imprime las ecuaciones de los modelos en un formato legible."""
    print("--- Ecuaciones de los Modelos de Regresión Lineal ---")
    for clase, modelo in modelos.items():
        nombre_clase = nombres_clases_es[clase]
        coeficientes = modelo.coef_
        intercepto = modelo.intercept_
        ecuacion = f"y = {intercepto:.4f}"
        for i, coef in enumerate(coeficientes):
            if coef >=0:
                signo = " + "
            else:
                signo = " - "
            ecuacion += f"{signo}{abs(coef):.4f} * {nombres_features_es[i]}"
        print(f"Modelo para la clase '{nombre_clase}':")
        print(ecuacion + "\n")
    print("=" * 70)

def exportar_excel(resultados):
    carpeta_salida = 'resultados'
    nombre_archivo = 'clasificacion_iris.xlsx'
    ruta_completa = os.path.join(carpeta_salida, nombre_archivo)
            
    try:
        resultados.to_excel(ruta_completa, index=False)
        print(f"Datos exportados exitosamente a '{ruta_completa}'")
    except Exception as e:
        print(f"Ocurrió un error al exportar el archivo: {e}")

def visualizar_importancia_caracteristicas(modelos, nombres_features_es, nombres_clases_es):
    """
    Genera un gráfico de barras mostrando la magnitud de los coeficientes por característica para cada modelo.
    """
    plt.figure(figsize=(12, 8))
    
    df_coefs = pd.DataFrame()
    for cls, model in modelos.items():
        df_coefs[nombres_clases_es[cls]] = model.coef_
    
    df_coefs.index = nombres_features_es
    
    # Graficar los coeficientes (magnitud absoluta para importancia)
    df_coefs.T.plot(kind='bar', figsize=(12, 7), colormap='viridis')
    plt.title('Importancia de las Características por Clase (Magnitud de Coeficientes)', fontsize=16)
    plt.xlabel('Clase de Flor', fontsize=12)
    plt.ylabel('Magnitud del Coeficiente', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Característica')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout() # Ajusta el layout para que no se corten las etiquetas

    carpeta_salida = 'imgs'
    ruta_grafico = os.path.join(carpeta_salida, 'importancia_caracteristicas.png')
    plt.savefig(ruta_grafico)
    print(f"\nGráfico de importancia de características guardado en '{ruta_grafico}'")
    plt.close()

def visualizar_precision_por_clase(y_test, y_pred, nombres_clases_es):
    """
    Genera un gráfico de barras de la precisión por clase y lo guarda como una imagen.
    """
    cm = confusion_matrix(y_test, y_pred)
    precision_por_clase = cm.diagonal() / cm.sum(axis=1)

    plt.figure(figsize=(8, 6))
    sns.barplot(x=nombres_clases_es, y=precision_por_clase, palette='viridis')
    plt.title('Precisión de Clasificación por Clase', fontsize=16)
    plt.xlabel('Clase de Flor', fontsize=12)
    plt.ylabel('Precisión (Correctas / Totales)', fontsize=12)
    plt.ylim(0, 1.1)
    plt.grid(axis='y', linestyle='--')
    for index, value in enumerate(precision_por_clase):
        plt.text(index, value + 0.05, f'{value:.2f}', ha='center', fontsize=10)

    carpeta_salida = 'imgs'

    # Guardar el gráfico como un archivo de imagen
    ruta_grafico = os.path.join(carpeta_salida, 'precision_por_clase.png')
    plt.savefig(ruta_grafico)
    print(f"\nGráfico de precisión guardado en '{ruta_grafico}'")
    plt.close() 

def main():

    # Cargar y preparar los datos
    X_train, X_test, y_train, y_test = cargar_y_dividir_datos()

    # Renombrar las clases y características
    nombres_clases_es = ['Setosa', 'Versicolor', 'Virginica']
    nombres_features_es = ['largo_sepalo', 'ancho_sepalo', 'largo_petalo', 'ancho_petalo']

    # Entrenar los modelos
    modelos_entrenados = entrenar_modelos(X_train, y_train)

    # Mostrar las ecuaciones de los modelos
    mostrar_ecuaciones(modelos_entrenados, nombres_features_es, nombres_clases_es)

    # Realizar predicciones y generar el DataFrame de resultados
    y_pred = predecir(X_test, modelos_entrenados)
    df_resultados = generar_resultados(X_test, y_test, y_pred, nombres_clases_es)
    exportar_excel(df_resultados)

    # Generar gráficos
    visualizar_importancia_caracteristicas(modelos_entrenados, nombres_features_es, nombres_clases_es)
    visualizar_precision_por_clase(y_test, y_pred, nombres_clases_es)

    # Precisión del modelo
    accuracy = np.mean(y_pred == y_test)
    print(f"\nPrecisión General del Modelo: {accuracy:.2f}\n")

    
if __name__ == "__main__":
    main()