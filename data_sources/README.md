# 📂 Data Sources

Este directorio contiene referencias y ejemplos de las fuentes de datos utilizadas en el proyecto. **Los archivos de datos completos no están incluidos en el repositorio debido a su tamaño**. Consulta las instrucciones para descargar y manejar los archivos desde sus respectivas fuentes.

---

## 📋 Contenido de la Carpeta

### 1. **Parques de Diversiones y Centros Comerciales**
   - **Archivos**:
     - `Parques de diversiones Centros comerciales 2014.csv` al `Parques de diversiones Centros comerciales 2024.csv`
   - **Descripción**:
     Contiene información sobre parques de diversiones y centros comerciales, como localización y características relevantes.
   - **Fuente**: Datos generados mediante análisis histórico y proyecciones.
   - **Instrucciones**:
     - Estos archivos ya están disponibles en esta carpeta y no requieren pasos adicionales.

---

### 2. **Unidades Educativas**
   - **Archivos**:
     - `unidades_educativas_2015.json` al `unidades_educativas_2024.json`
   - **Descripción**:
     Incluye datos sobre la ubicación y características de las unidades educativas durante distintos años.
   - **Fuente**: API de Overpass.
   - **Instrucciones**:
     - Los datos están listos para ser utilizados directamente en los scripts de ETL.
    

---

### 3. **Restaurantes**
   - **Archivo**:
     - `restaurantes_overpass_2023.json` y `restaurantes_overpass_2023.json'.
   - **Descripción**:
     Contiene información de restaurantes, como su ubicación y datos relevantes.
   - **Fuente**: Overpass API.
   - **Instrucciones**:
     - Puedes reutilizar el archivo actual o generar nuevos datos usando la consulta almacenada en la carpeta `queries`.

---

### 4. **Metadata de Sitios**
   - **Archivos Externos**:
     - `metadata-sitios-20250114T225354Z-001.zip`
     - `metadata-sitios-20250114T225354Z-002.zip`
   - **Descripción**:
     Contiene información de servicios comerciales, incluyendo su ubicación y características.
   - **Fuente**: Google Drive.
   - **Instrucciones para Acceso**:
     1. Descarga los archivos desde [Google Drive](https://drive.google.com/drive/folders/1olnuKLjT8W2QnCUUwh8uDuTTKVZyxQ0Z?usp=drive_link).
     2. Descomprime los archivos y colócalos en esta carpeta.

---

### 5. **Reseñas de Florida**
   - **Archivo Externo**:
     - `review-Florida.zip`
   - **Descripción**:
     Contiene reseñas de usuarios sobre servicios comerciales de Florida.
   - **Fuente**: Google Drive.
   - **Instrucciones para Acceso**:
     1. Descarga el archivo desde [Google Drive](https://drive.google.com/drive/folders/1kxYcx3BjWNR2IVJ9odksaPRVOWzwQJts?usp=drive_link).
     2. Descomprime el archivo y colócalo en esta carpeta.

---

### 6. **Yelp Dataset**
   - **Archivos**:
     - `yelp_dataset/business.json`
     - `yelp_dataset/review.json`
   - **Descripción**:
     Datos sobre negocios, reseñas y usuarios de Yelp.
   - **Fuente**: [Yelp Open Dataset](https://www.yelp.com/dataset).
   - **Instrucciones para Acceso**:
     1. Descarga el archivo desde el enlace proporcionado.
     2. Descomprime el archivo y organiza los datos bajo el directorio `yelp_dataset`.

---

### 7. **Datos de la API de Google**
   - **Archivo Generado**:
     - `datos_api_google.csv`
   - **Descripción**:
     Contiene información geográfica de servicios comerciales en Florida generada mediante la API de Google.
   - **Fuente**: Generado por el script `descarga_datos_API.ipynb`.
   - **Instrucciones**:
     1. Ejecuta el script en la carpeta `etl_pipeline`.
     2. Cambia los parámetros según la geolocalización deseada.
     3. Une los datos generados con los archivos procesados de `metadata-sitios` 
        y unelos a los archibos descargados de google.

---

## 🌐 Fuentes de Datos

1. **Google Drive**:
   - Enlace para archivos principales: [Google Drive](https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA).

2. **Yelp Open Dataset**:
   - [Descarga aquí](https://www.yelp.com/dataset).

3. **Overpass API**:
   - [Documentación oficial](https://wiki.openstreetmap.org/wiki/Overpass_API).

---

## 🛠️ Notas Técnicas

1. **Archivos Externos**:
   - Los archivos grandes no están incluidos en este repositorio. Descárgalos desde los enlaces proporcionados.
2. **Formato Esperado**:
   - Asegúrate de que los archivos mantienen su formato original para garantizar compatibilidad.
3. **Actualizaciones**:
   - Documenta cualquier archivo nuevo o cambios relevantes en este archivo.

---




