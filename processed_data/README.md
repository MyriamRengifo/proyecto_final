# 📂 Processed Data

Este directorio contiene los datos procesados y limpios generados durante la fase de ETL. Estos archivos son el resultado de transformar las fuentes de datos originales en formatos estructurados listos para análisis y modelado.

---

## 📋 Contenido de la Carpeta

### 1. **Archivo Principal**

- **`servicio_restaurantes.csv`**  
  Contiene información detallada sobre servicios de restaurantes procesados desde las fuentes originales. Las columnas incluidas son:

  - `id_servicios_restaurantes`: ID único para cada establecimiento.  
  - `servicios_restaurantes`: Nombre del establecimiento.  
  - `direccion`: Dirección del establecimiento.  
  - `id_condado`: ID único del condado.  
  - `condado`: Nombre del condado.  
  - `codigo_postal_condado`: Código postal del condado.  
  - `latitud_condado`: Latitud del condado.  
  - `longitud_condado`: Longitud del condado.  
  - `id_ciudad`: ID único de la ciudad.  
  - `ciudad`: Nombre de la ciudad.  
  - `codigo_postal_ciudad`: Código postal de la ciudad.  
  - `latitud_ciudad`: Latitud de la ciudad.  
  - `longitud_ciudad`: Longitud de la ciudad.  
  - `estado`: Estado de la ciudad.  
  - `categorias`: Categoría del restaurante (tipo de comida).  
  - `puntuacion_usuarios`: Puntuación otorgada por los consumidores.  
  - `analisis_sentimientos`: Análisis de sentimientos basado en opiniones de los consumidores.  
  - `url_del_negocio`: Dirección web del negocio.  
  - `anio`: Año en que se recolectaron los datos.  

---

### 2. **Archivos de Servicios Secundarios**

- **`servicio_tiendas_negocio.csv`**  
  Información geográfica sobre tiendas y negocios en el área de Florida.  

- **`servicio_transporte.csv`**  
  Datos sobre servicios de transporte disponibles en el estado de Florida.  

- **`servicios_educacion.csv`**  
  Servicios relacionados con educación, listos para su integración en visualizaciones.  

- **`servicios_entretenimiento.csv`**  
  Agrupación de servicios relacionados con entretenimiento, como cines, centros comerciales, parques y teatros.  

- **`servicios_hospedaje.csv`**  
  Datos relacionados con hostelería, como hoteles y alojamientos.  

Estos archivos contienen las mismas columnas que el archivo principal, adaptadas al tipo de servicio específico.

---

### 3. **Dimensiones (Datos de Referencia)**

- **`ciudades_dim.csv`**  
  Contiene información sobre condados y ciudades. Las columnas son:
  - `id_condado`: ID único del condado.  
  - `condado`: Nombre del condado.  
  - `codigo_postal_condado`: Código postal del condado.  
  - `latitud_condado`: Latitud del condado.  
  - `longitud_condado`: Longitud del condado.  
  - `id_ciudad`: ID único de la ciudad.  
  - `ciudad`: Nombre de la ciudad.  
  - `codigo_postal_ciudad`: Código postal de la ciudad.  
  - `latitud_ciudad`: Latitud de la ciudad.  
  - `longitud_ciudad`: Longitud de la ciudad.  

- **`servicio_restaurantes_dim.csv`**  
  Dimensión de restaurantes que incluye:  
  - `id_servicios_restaurantes`: ID único del restaurante.  
  - `servicios_restaurantes`: Nombre del restaurante.  

- **`servicio_tiendas_negocio_dim.csv`**  
  Dimensión que agrupa tiendas y negocios:  
  - `id_centros_tiendas_negocio`: ID único del negocio.  
  - `centros_tiendas_negocio`: Nombre del negocio.  

- **`centros_hosteleria_dim.csv`**  
  Contiene información dimensional sobre centros de hostelería:  
  - `id_centros_hosteleria`: ID único del centro de hostelería.  
  - `centros_hosteleria`: Nombre del centro.  

- **`centros_educacion_dim.csv`**  
  Contiene información dimensional sobre centros educativos:  
  - `id_centros_educacion`: ID único del centro educativo.  
  - `centros_educacion`: Nombre del centro educativo.  

- **`centros_entretenimiento_dim.csv`**  
  Información estructurada sobre centros de entretenimiento:  
  - `id_centros_entretenimiento`: ID único del centro de entretenimiento.  
  - `centros_entretenimiento`: Nombre del centro de entretenimiento.

- **`servicio_trasporte_dim.csv`**  
  Información estructurada sobre centros de entretenimiento:  
  - `id_trasporte`: ID único del servicio de trasporte.  
  - `trasporte`: Nombre del servicio de trasporte. 
---

## 🛠️ Notas Técnicas

1. **Origen de los Datos**:  
   - Estos archivos fueron generados a partir de las transformaciones realizadas en los scripts de ETL, combinando datos de múltiples fuentes almacenadas en `data_sources`.

2. **Formato de los Archivos**:  
   - Todos los archivos están en formato **`.csv`** y codificados en **UTF-8**.
   - Los separadores de columnas son comas (`,`).

3. **Compatibilidad**:  
   - Los archivos están diseñados para ser utilizados en herramientas como Power BI, Tableau y Python para análisis avanzado.

4. **Estructura General**:  
   - Cada archivo contiene columnas clave que permiten su integración con otras tablas, como `id`, `nombre`, `categoría` y `ubicación`.

---

😊

