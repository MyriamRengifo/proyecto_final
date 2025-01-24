# 📂 Carga y Transformación de Datos

## 📄 Descripción
El notebook **carga y transformación de datos.ipynb** está diseñado para:
- Cargar archivos desde el **Databricks File System (DBFS)**.
- Transformar los datos en formato **Delta**.
- Almacenarlos en el **Unity Catalog** de Databricks, optimizando los datos para su análisis y consultas.

---

## 🛠️ Funcionalidades Principales

1. **Listar Archivos Disponibles**  
   - Verifica y lista los archivos cargados en la ruta especificada del **DBFS**.

2. **Carga de Archivos**  
   - Lee los datos desde archivos CSV utilizando **Spark DataFrames** con detección automática de esquemas.

3. **Transformación a Delta Tables**  
   - Convierte los archivos CSV en **Tablas Delta**, almacenándolos en el **Unity Catalog**.

4. **Validación de Tablas**  
   - Verifica la creación de las tablas Delta mediante comandos SQL.

5. **Inspección de Datos Crudos**  
   - Inspecciona la estructura de los datos almacenados en el sistema de archivos de Databricks (**DBFS**).

---

## 📋 Proceso de Ejecución

### 1. **Listar Archivos en DBFS**
   - El notebook utiliza `dbutils.fs.ls()` para verificar los archivos disponibles en la ruta:  
     `dbfs:/Volumes/aprendisaje/default/servicios2/`.

### 2. **Carga y Procesamiento de Archivos**
   - Los datos procesados incluyen información sobre servicios educativos, entretenimiento, transporte y restaurantes.

### 3. **Creación de Tablas Delta**
   - Los archivos son cargados como **Spark DataFrames**, procesados y almacenados como tablas Delta dentro del esquema:  
     `aprendisaje.default`.

### 4. **Validación de Tablas**
   - Comando SQL para listar y validar las tablas creadas:  
     ```sql
     SHOW TABLES IN aprendisaje.default;
     ```

### 5. **Inspección de Datos Crudos**
   - Comando para inspeccionar los archivos en DBFS:  
     ```python
     dbutils.fs.ls("dbfs:/mnt/ingest_data/raw/")
     ```

---

## 📁 Archivos Procesados

Los siguientes archivos son procesados y convertidos a tablas Delta:

- `centros_educacion_dim.csv`  
- `centros_entretenimiento_dim.csv`  
- `centros_hosteleria_dim.csv`  
- `ciudades_dim.csv`  
- `servicio_restaurantes.csv`  
- `servicio_tiendas_negocio_dim.csv`  
- `servicio_tiendas_negocios.csv`  
- `servicio_transporte.csv`  
- `servicio_transporte_dim.csv`  
- `servicios_educacion.csv`  
- `servicios_entretenimiento.csv`  
- `servicios_hospedaje.csv`  
- `servicios_restaurantes_dim.csv`  

---

## 🌟 Ventajas del Proceso

1. **Optimización del Rendimiento:**  
   - Mejora la velocidad y eficiencia de las consultas utilizando tablas Delta.

2. **Estandarización de Datos:**  
   - Garantiza un formato estructurado y consistente para todos los datos.

3. **Automatización:**  
   - Simplifica y acelera el proceso de carga y transformación.

4. **Flexibilidad:**  
   - Permite añadir nuevos archivos fácilmente al flujo.

---

## 🚨 Notas Importantes

1. **Configuración Inicial:**  
   - Asegúrate de que los archivos estén en la ruta especificada antes de ejecutar el notebook.

2. **Validación de Rutas:**  
   - Verifica que los nombres y rutas de los archivos sean correctos.

3. **Consistencia de Esquemas:**  
   - Asegúrate de que los esquemas de los datos sean consistentes para evitar errores.

---

Con este notebook, simplificamos y estandarizamos el proceso de carga y transformación de datos en Databricks, asegurando que los datos estén listos para análisis avanzados y modelado. 🚀
😊
