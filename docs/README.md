📁 Proyecto
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
│   │   ├── metadata_sitios.ipynb # Datos extraídos con Google API
│   │   └── merge_archivos.ipynb  # Unificación de los datos procesados.
│   ├── queries               # Consultas específicas para extracción de datos
│   │   └── overpass_query.overpassql  # Consulta de Overpass API
│   │    
│   └── README.md             # Descripción del proceso ETL y cómo ejecutarlo
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
├── 📁 ml_pipeline          # Scripts y datos específicos para Machine Learning
│   ├── datasets            # Datos de entrenamiento generados
│   │   ├── train_data.csv
│   │   ├── test_data.csv
│   │   └── validation_data.csv
│   ├── scripts
│   │   ├── train_model.py         # Entrenamiento del modelo
│   │   ├── evaluate_model.py      # Evaluación del modelo
│   │   ├── predict.py             # Predicciones y uso del modelo
│   │   └── config.py              # Configuración de hiperparámetros
│   └── README.md                  # Documentación del pipeline de ML
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
│   ├── streamlit
│   │   ├── app.py                # Código para la presentación en Streamlit
│   │   ├── data/                 # Datos utilizados para la presentación
│   │   └── README.md             # Documentación del proyecto en Streamlit
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
│   ├── test_ml_pipeline.py
│   └── test_visualization.py
│
├── .gitignore              # Archivos y carpetas a excluir del repositorio
├── LICENSE                 # Licencia del proyecto
├── README.md               # Descripción general del proyecto
└── requirements.txt        # Dependencias del proyecto
