# 📁 Proyecto-Ingenieria-Datos

```plaintext
📁 Proyecto-Ingenieria-Datos
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
│   ├── notebooks
│   │   ├── ml_pipeline.dbc
│   │   └── data_analysis.dbc
│   ├── scripts
│   │   ├── automl_pipeline.py
│   │   └── clustering_model.py
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
│
├── .gitignore              # Archivos y carpetas a excluir del repositorio
├── LICENSE                 # Licencia del proyecto
├── README.md               # Descripción general del proyecto
└── requirements.txt        # Dependencias del proyecto
