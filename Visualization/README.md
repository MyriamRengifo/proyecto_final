![Portada](https://github.com/MyriamRengifo/proyecto_final/blob/Main/Visualization/Imagenes/Portada.jpg)

# VISUALIZACIÓN DE DATOS

# Indice:
   - Objetivos del proyecto
   - Contenido de la carpeta
   - Notas técnicas
   - Soporte y contribución

---
# 🎯 I) Objetivos del proyecto
Generar un dashboard que muestre de manera gráfica y resumida los principales insigths del proyecto, además de obtener métricas de interés para el negocio (KPI's).

Esto se logra luego del análisis detallado de los datos referentes a restaurantes, puntuaciones de usuarios y categorías más populares en diferentes condados y ciudades, identificando tendencias y áreas estratégicas para la toma de decisiones empresariales con respecto al rubro gastronómico.

Se resume en 3 aspectos clave:

- Análisis temporal por ciudad y su condado. KPI's de interés para el rubro.
- Análisis de categorías y distribución de restaurantes.
- Identificación de nichos relevantes para oportunidades de negocio.
---

# 📂 II) Contenido de la carpeta

Aqui se encuentran los archivos necesarios para generar el dashboard, donde se muestran los principales hallazgos de los diferentes datasets:
- Notebooks
- Enlaces a recursos externos
- Resultados

### 1. **Notebooks y scripts**
Los notebooks se encuentran organizados por fuente de datos y propósito:

- **KPI**:
  - `KPI_LuisMata.ipynb`: Exploracion y transformación de datos para obtener datos que permitan definir métricas de interés para el negocio.
  - `results_kpi1.csv, results_kpi2.csv, results_kpi3.csv`: resultados de tendencias necesarios para definir métrica objetivo.

- **Dashboard**:
  - `Streamlit_script to publish.py`: 
  - `.ipynb`: notebook utilizado para realizar el análisis de los distintos dataframes y generar resultados que posteriormente son parte del dashboard.

### 2. **Recursos externos**
  - Dashboard en streamlit [link](https://pruebapf.streamlit.app/)

 
# 🛠️ III) Notas Técnicas: 

1. **Requisitos**:📋
   - Contar con una cuenta en Streamlit para poder visualizar.
   - Tener instalado Power BI desktop, Power BI (deseable, no excluyente)


2. **Ejemplo de visualizaciones:** 📈 

Al graficar, optar por un enfoque que permita visualizar en un solo gráfico la mayor cantidad de información posible, por ejemplo:

![Gráfico de tendencia](https://github.com/MyriamRengifo/proyecto_final/blob/Main/Visualization/Imagenes/Tendencia_buena%20puntuacion.png)

En el  mismo podemos visualizar:
- Tendencia global
- Distribución de los datos
- Media de los datos año a año

# . IV) Conclusiones: 
  **Análisis de Puntuaciones y Oportunidades de Mercado**

1. **KPI de Puntuaciones**
- **Puntuación Promedio de Usuarios:** 4.18, logrando el objetivo mínimo establecido.
- **Porcentaje de Buenas Puntuaciones:** Solo el 65.1% de los restaurantes alcanzan puntuaciones "buenas", por debajo del objetivo del 68%.
- **Incremento en Reviews:** No se cumplió el objetivo, con un déficit del 89%.

2. **Tendencias de Puntuaciones**
- El promedio anual de puntuación muestra un ligero crecimiento, con una mayor pendiente entre 2022 y 2023.
- A partir de 2024, el crecimiento se estabiliza levemente.

3. **Análisis de Ciudades para 2024**
- *Mejor puntuación promedio:* Malone.
- *Peor puntuación promedio:* Ybor City.
- *Ciudades con mayor cantidad de restaurantes:* Miami, Orlando y Jacksonville.
- *Ciudades con menos restaurantes:* Lee, Jasper y Waldo.

4. ** Análisis de Nichos (2022-2024)**
- Top 5 ciudades con pocos restaurantes y puntuaciones excelentes: Bay Harbor Islands, Malone, Montverde, Seacrest y Shalimar.

5. **Distribución y Categorías**
- Los condados con mayor cantidad de restaurantes suelen tener puntuaciones promedio más altas.
- Las categorías más populares en 2024 incluyen:
  - Restaurantes y Servicios.
  - Bares y Vida Nocturna.
  - Fast Food.
  - Cocina Caribeña y Latina.

6. **Oportunidades de Mercado**
- Las ciudades con pocos restaurantes y altas puntuaciones representan grandes oportunidades para expansión.
- Las categorías populares son clave para identificar tendencias de mercado y áreas de enfoque estratégico.


---

## 👷🏽👷🏽‍♀️ IV) Soporte y contribución:
   - **Angélica Cassano**: Data Analyst
   ![Github](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white&style=flat-square) [Github](https://github.com/Halsey26)
   ![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?logo=linkedin&logoColor=white&style=flat-square) [LinkedIn](https://www.linkedin.com/in/angelica-cassano/)
   
   - **Luis Mata**: Data Analyst
   ![Github](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white&style=flat-square) [Github](https://github.com/AutoMataX)
   ![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?logo=linkedin&logoColor=white&style=flat-square) [LinkedIn](https://www.linkedin.com/in/matasanchez999/)
   




