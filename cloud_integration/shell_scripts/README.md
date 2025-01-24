# Shell Scripts - Configuración y Transferencia con Databricks

## 📄 Descripción
Este directorio contiene scripts de shell diseñados para automatizar la configuración y transferencia de datos entre tu PC y el entorno **Azure Databricks**. Los scripts permiten:
- Configurar tokens de acceso necesarios para interactuar con Databricks.
- Subir archivos desde la PC al **Databricks File System (DBFS)**.
- Descargar archivos desde Databricks a tu PC.

---

## 📁 Archivos en la Carpeta

### 1. `configurar_databricks.sh`
- **Propósito:** Configura la autenticación mediante token y facilita la transferencia de archivos.
- **Funciones Principales:**
  - Configurar automáticamente la CLI de Databricks con tokens y URL del workspace.
  - Subir archivos desde la PC al DBFS.
  - Descargar archivos del DBFS a la PC.

---

## 🚀 Cómo Usar el Script

### Requisitos Previos
1. **Databricks CLI:** Asegúrate de tener la CLI instalada:
   ```bash
   pip install databricks-cli
   ```
2. **Permisos**: Da permisos de ejecución al script:
   ```bash
   chmod +x configurar_databricks.sh
   ```
- **Variables del Script**

Antes de ejecutar el script, actualiza las siguientes variables en el archivo configurar_databricks.sh:

   - DATABRICKS_URL: URL del workspace de Databricks 
   - DATABRICKS_TOKEN: Token personal generado en Databricks para autenticación.
   - credenciales.txt: Documento donde se copia el token
   - LOCAL_FILE_PATH: Ruta del archivo en tu PC que deseas subir.
   - DATABRICKS_DEST_PATH: Ruta de destino en el DBFS (Databricks File System).
   - DATABRICKS_SRC_PATH: Ruta del archivo en el DBFS que deseas descargar.
   - LOCAL_DEST_PATH: Ruta donde se descargará el archivo en tu PC.

Comandos Básicos

- ** Configurar Databricks CLI:**
```bash
./configurar_databricks.sh
```
- **Transferir Archivos:**

 -  Subir un archivo desde tu PC a Databricks:
```bash
./configurar_databricks.sh
 ```
 - Descargar un archivo desde Databricks a tu PC:
 ```bash
./configurar_databricks.sh
```
### 🌟 Funciones del Script
1. Configuración de la CLI de Databricks

El script configura automáticamente la CLI de Databricks utilizando el token y la URL proporcionados.
2. Subida de Archivos

Permite transferir archivos desde tu PC al DBFS (Databricks File System), facilitando la integración de datos en tus pipelines.
3. Descarga de Archivos

Facilita la descarga de resultados y datos procesados desde Databricks a tu máquina local.
🛠️ Ejemplo de Uso
- ## Caso: Subir un Archivo

Si tienes un archivo dataset.csv en la ruta /home/user/datos/ que deseas subir al DBFS, ajusta las variables en el script:
```bash
LOCAL_FILE_PATH="ruta del archivo a subir"
DATABRICKS_DEST_PATH="ruta del almasenamiento de los datos"

- Ejecuta el script:

```bash
./configurar_databricks.sh
```
- ## Caso: Descargar un Archivo

Si tienes un archivo en el DBFS ubicado en /mnt/datos/salida.csv y quieres descargarlo a tu PC, ajusta las variables:
```bash
DATABRICKS_SRC_PATH="ruta del almasenamiento de los datos"
LOCAL_DEST_PATH="la ruta donde se guardara los achivos en local"
```
- Ejecuta el script:
```bash
./configurar_databricks.sh
```
### 📋 Notas Adicionales

# Seguridad: Asegúrate de mantener tus tokens de acceso seguros. No compartas el archivo configurar_databricks.sh ni el archivo credenciales.txt sin eliminar primero los valores sensibles.

# Errores Comunes:
 - Si la CLI de Databricks no está instalada, el script fallará.
 - Asegúrate de que las rutas proporcionadas sean correctas.

 😊