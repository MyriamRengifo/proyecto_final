# 📂 ETL Pipeline

Esta carpeta contiene los archivos necesarios para el proceso de extracción, transformación y carga (ETL) del proyecto. Incluye notebooks, consultas específicas y scripts para integrar las diferentes fuentes de datos.

---

## 📋 Contenido de la Carpeta

### 1. **Notebooks**
Los notebooks se encuentran organizados por fuente de datos y propósito:

- **Google API**:
  - `metadata_sitios.ipynb`: Obtención de datos de servicios y  localización mediante las APIs de Google.

- **Overpass API**:
  - `overpass_restaurantes.ipynb`: Extracción de datos de restaurantes usando Overpass API.
  - `Parques de diversiones Centros comerciales.ipynb`: Extracción de datos de parques de diversiones y centros comerciales usando Overpass API.
  - `unidad educativa.ipynb`: Extracción de datos sobre unidades educativas.

- **Yelp Open Dataset**:
  - `ETL_yelp.ipynb`: Transformación y limpieza de datos del dataset de Yelp usando Overpass API.

- **Unificación de Datos**:
  - `merge_archivos.ipynb`: Unifica los datos de Google, Yelp y Overpass en un único formato procesado.

---

### 2. **Consultas (`queries`)**
Esta subcarpeta contiene las consultas utilizadas para la extracción de datos desde Overpass API:

- `overpass_parques_de_diversiones_centrocomerciales_query.overpassql`: Consulta para extraer información de parques y centros comerciales del 2014 al 2024.
- `overpass_unidades_educativas_query.overpassql`: Consulta para extraer datos de unidades educativas del 2014 AL 2024.
- `overpass_restaurants_query.overpassql`: Consulta para extraer datos de restaurantes en 2022 Y 2023.

Las consultas están formateadas para ser utilizadas directamente en Overpass API ,OpenStreetMap,en overpass se nesecita analizar marcas de tiempo (timestamp) en el resultado JSON..

---

## 🛠️ Notas Técnicas

1. **Requisitos**:  
   - Asegúrate de tener configurado un entorno Python con Jupyter Notebook para ejecutar los archivos `.ipynb`.
   - Algunas consultas requieren conexión a internet para comunicarse con Overpass API o Google API.

2. **Dependencias**:  
   - Los notebooks utilizan bibliotecas como `pandas`, `requests`, y `geopy`. Asegúrate de instalar las dependencias incluidas en `requirements.txt`.

3. **Proceso de ETL**:  
   - Ejecuta los notebooks por orden lógico:  
     1. Obtención de datos con **Overpass API**, **Google API** y **Yelp**.  
     2. Procesamiento individual de los datos.  
     3. Unificación de los datos con el archivo `merge_archivos.ipynb`.

---
😊
