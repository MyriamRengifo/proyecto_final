# 📂 ML Pipeline

## 📄 Descripción

El directorio **ML Pipeline** contiene notebooks y scripts orientados a la creación, entrenamiento y evaluación de modelos de Machine Learning. Su objetivo principal es predecir el puntaje de restaurantes basado en características geográficas y métricas clave, proporcionando una herramienta robusta para comprender y proyectar datos en el sector gastronómico.

---

## 🚀 Propósito de los Archivos

### 1. **`datasets/`**
- Contiene los datos preprocesados en formato **Parquet**.
- **Archivos clave**:
  - `florida_cities.parquet`: Datos de ciudades en Florida.
  - `florida_restaurants.parquet`: Información de restaurantes.
  - `florida_yearly.parquet`: Datos agregados por año.

### 2. **`ML_1_entrenamiento_modelo.ipynb`**
- **Propósito**: Entrenar un modelo **KNN (K-Nearest Neighbors)** para predecir puntajes de restaurantes.
- **Características principales**:
  - Configuración y ajuste de hiperparámetros utilizando `GridSearchCV`.
  - Métricas de evaluación como **MSE**.
  - Visualización de resultados y predicciones con mapas interactivos usando **Folium**.
  - Creación de un modelo de predicción basado en coordenadas geográficas.

### 3. **`ML_1_seleccion_datos.ipynb`**
- **Propósito**: Realizar análisis exploratorio de datos y preparar las variables para el modelo.
- **Características principales**:
  - Visualización de distribuciones mediante gráficos de densidad con **Seaborn**.
  - Representación geográfica de datos utilizando **Basemap**.

### 4. **`ML_1.py`**
- **Propósito**: Implementar el modelo en un script ejecutable para integración en producción.
- **Características principales**:
  - Lógica compacta para entrenar y realizar predicciones.
  - Optimización del modelo KNN y generación de mapas interactivos.

### 5. **`exploracion_gmf.ipynb`**
- **Propósito**: Explorar tendencias a lo largo de los años utilizando un modelo de regresión polinómica.
- **Características principales**:
  - Proyección de puntajes basados en categorías específicas de restaurantes.
  - Uso de `GrandMeansForecaster` para realizar pronósticos.
  - Visualización de tendencias y diferencias año a año.

---

## 📋 Ejecución de los Archivos

### **1. Cargar los Datos**
- Los archivos **Parquet** en la carpeta `datasets/` son utilizados como entrada para los notebooks.

### **2. Orden de Ejecución**
1. **`ML_1_seleccion_datos.ipynb`**: Explora y selecciona variables para el modelo.
2. **`ML_1_entrenamiento_modelo.ipynb`**: Ajusta y entrena el modelo KNN.
3. **`ML_1.py`**: Integra la lógica en un script ejecutable para producción.

### **3. Visualización**
- Ejecuta **`ML_1_entrenamiento_modelo.ipynb`** para generar mapas interactivos y métricas del modelo.

### **4. Exploración Avanzada**
- Usa **`exploracion_gmf.ipynb`** para proyectar tendencias y visualizar cambios en el tiempo.

---

## 🌟 Beneficios del Pipeline

- **Predicciones precisas**: Utiliza KNN optimizado para predecir puntajes según la ubicación.  
- **Visualización geográfica**: Genera mapas interactivos para interpretar resultados y patrones.  
- **Tendencias a largo plazo**: Proyección de datos basada en categorías y cambios históricos.  
- **Automatización y escalabilidad**: Flujo fácilmente integrable con pipelines en producción.  

---

## 📝 Notas Adicionales

### Dependencias
Asegúrate de instalar los siguientes paquetes antes de ejecutar los notebooks:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn folium basemap
```
---
😊
