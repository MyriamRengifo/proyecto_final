# 📁  DataZoo: Transformando Datos en Decisiones 

```
📁 DATAZOO
├── 📁 data_sources          # Fuentes de datos originales o ejemplos de datos
│   ├── README.md
│   ├── yelp_data_sample.csv  
│   ├── google_data_sample.csv
│   └── overpass_data_sample.csv
│
├── 📁 etl_pipeline           # Proceso de extracción, transformación y carga
│   ├── notebooks             # Notebooks utilizados en el proceso ETL
│   │   ├── yelp_etl.ipynb
│   │   ├── google_etl.ipynb
│   │   ├── overpass_etl.ipynb  # Notebook usado para descargar datos con Overpass API
│   │   └── README.md          # Explicación de los notebooks
│   ├── queries               # Consultas específicas para extracción de datos
│   │   ├── overpass_query.overpassql  # Consulta de Overpass API
│   │   └── other_queries.sql          # Otras consultas SQL si aplica
│
├── 📁 eda                  # Análisis exploratorio de datos
│   ├── yelp_eda.ipynb
│   ├── google_eda.ipynb
│   ├── overpass_eda.ipynb
│   └── README.md
│
├── 📁 processed_data        # Archivos procesados y limpios
│   ├── yelp_clean.csv
│   ├── google_clean.csv
│   ├── overpass_clean.csv
│   └── README.md
│
├── 📁 cloud_integration    # Integración con Azure Databricks
│   ├── jobs/
│   │   ├── 1.Configuración del ETL.ipynb
|   |   ├── 2.Cargar tablas delta.ipynb
|   |   ├── 3.limpiar los archivos de ingreso.ipynb
|   |   ├── 4.creación de informe con todo lo hecho anteriormente.ipynb
|   |   ├── conteo de datos.ipynb
│   │   └── README.md                   # Documentación del directorio
│   ├── notebooks/
│   │   ├── carga_y_transformacion_datos.ipynb  # Notebook principal para carga ytransformación de datos.
│   │   └── README.md                          # Documentación detallada del notebook y su uso.
|   ├── shell_scripts/
|   |    ├── configurar_databricks.sh # Script principal para configuración y transferencia
|   |    ├── credenciales.txt            # Archivo donde se almacenan los tokens )
|   |    └── README.md                   # Documentación del directorio
|   |
│   └── README.md
│
├── 📁 visualization        # Visualización y análisis
│   ├── power_bi_reports
│   │   ├── sales_dashboard.pbix
│   │   └── location_analysis.pbix
│   ├── plots
│   │   ├── sales_trends.png
│   │   └── customer_segmentation.png
│   └── README.md
│
├── 📁 local_development    # Archivos locales y herramientas de VS Code
│   ├── environment.yml
│   ├── config.json
│   └── main.py
│
├── 📁 docs                 # Documentación del proyecto
│   ├── project_overview.md
│   ├── architecture_diagram.png
│   ├── api_usage.md
│   └── contributing.md
│
├── 📁 tests                # Pruebas unitarias y de integración
│   ├── test_etl.py
│   ├── test_ml_pipeline.py
│   └── test_visualization.py
|
├── 📁 imagenes
│   ├── logos/
│   ├── dashboards/
│   └── resultados/
|
├── .gitignore              # Archivos y carpetas a excluir del repositorio
├── LICENSE                 # Licencia del proyecto
├── README.md               # Descripción general del proyecto
└── requirements.txt        # Dependencias del proyecto
