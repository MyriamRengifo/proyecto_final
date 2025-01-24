# 📂 Jobs - Scripts y Procesos de Trabajo en Databricks

## 📄 Descripción

Este directorio contiene los notebooks utilizados para ejecutar los procesos de trabajo (**jobs**) en **Databricks**, organizados de manera secuencial. Estos notebooks están diseñados para automatizar y estructurar tareas clave en el flujo de datos, desde la configuración inicial hasta la generación de informes.

---

## 📁 Archivos en la Carpeta

1. **`1.Configuración del ETL.ipynb`**
   - **Propósito:** Configura el entorno necesario para el pipeline ETL.
   - **Funciones Principales:**
     - Carga inicial de datos desde **DBFS**.
     - Configuración de parámetros para el flujo de datos.

2. **`2.Cargar tablas delta.ipynb`**
   - **Propósito:** Procesa y almacena los datos en formato **Delta Table** dentro de Databricks.
   - **Funciones Principales:**
     - Conversión de datos procesados a **Delta Table**.
     - Configuración de particiones para optimizar consultas.

3. **`3.limpiar los archivos de ingreso.ipynb`**
   - **Propósito:** Elimina o transforma registros erróneos en los archivos cargados.
   - **Funciones Principales:**
     - Validación de la calidad de los datos.
     - Limpieza de datos duplicados o inconsistentes.

4. **`4.creación de informe con todo lo hecho anteriormente.ipynb`**
   - **Propósito:** Resume y genera informes visuales de los procesos realizados anteriormente.
   - **Funciones Principales:**
     - Resumen estadístico del pipeline.
     - Generación de gráficos y tablas clave para reportes.

5. **`conteo de datos.ipynb`**
   - **Propósito:** Realiza el conteo de filas en el archivo `servicios_restaurantes` antes y después de la descarga.
   - **Funciones Principales:**
     - Comparación de la cantidad de datos procesados.
     - Validación del flujo de datos y detección de posibles pérdidas.

---

## 🚀 Cómo Usar los Notebooks

1. **Secuencia de Ejecución**
   - Sigue el orden numérico para garantizar que los procesos se ejecuten correctamente:
     - Comienza con `1.Configuración del ETL.ipynb`.
     - Finaliza con `4.creación de informe con todo lo hecho anteriormente.ipynb`.

2. **Requisitos Previos**
   - Los datos deben estar cargados en **DBFS** antes de iniciar los procesos.
   - Asegúrate de tener acceso a los recursos y permisos necesarios en Databricks.

3. **Ejecución**
   - Crea los trabajos en la sección de **Jobs** de Databricks utilizando los notebooks de manera secuencial.
   - Programa los triggers para que la actualización se realice automáticamente en el día y la hora indicados.

---

## 📋 Notas Adicionales

- **Versionamiento:** Todos los notebooks están preparados para ser integrados en flujos automatizados de trabajo.
- **Errores Comunes:**
  - Revisa que las rutas de los archivos en **DBFS** estén correctamente configuradas en el notebook `1.Configuración del ETL.ipynb`.
  - Asegúrate de que los datos de entrada coincidan con las especificaciones de cada notebook.

---

Este archivo README proporciona una guía clara y estructurada para comprender y ejecutar los procesos almacenados en esta carpeta. Ideal para documentar y mantener un flujo de trabajo organizado en Databricks. 😊
