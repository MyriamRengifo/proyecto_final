import streamlit as st
st.set_page_config(
        page_title="Principal",
        page_icon=":material/favorite:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
st.sidebar.page_link("02_Asistente_de_predicción.py", label="Your profile")


# Título del proyecto y dashboard
st.markdown("# 📊 Análisis Estratégico de Restaurantes en Florida - EE.UU")

# Introducción
st.markdown("""
            -------
            Este dashboard ofrece un análisis detallado de los restaurantes, puntuaciones de usuarios y categorías más populares en diferentes condados y ciudades. 
            A través de gráficos y KPI, se identifican tendencias clave y áreas estratégicas para la toma de decisiones empresariales.
            -------
            """)
# Texto complementario
st.markdown("""
El análisis se divide en tres secciones principales:

- **KPI y Análisis de Puntuaciones:**  
   Indicadores clave de rendimiento (KPI) de puntuaciones y análisis temporal por ciudad y condado.

- **Distribución de Restaurantes:**  
   Exploración de categorías y distribución de restaurantes por ciudades. Además, un mapa interactivo facilita la identificación de zonas con puntuaciones promedio más altas.

- **Nichos Relevantes:**  
   Identificación de nichos de mercado. Esta sección destaca áreas con pocos restaurantes pero puntuaciones promedio altas, subrayando oportunidades para nuevos negocios.
""")

pbi_url = "https://app.powerbi.com/view?r=eyJrIjoiNTlhYTQxMWEtZDMxMS00ZjhmLWIxNWQtOGMwZTI3ZGQ3OGViIiwidCI6IjljNWM4NjYyLTFiZjUtNGU5NC1hODIwLTVlM2NhMTI2Zjc1MiIsImMiOjR9&pageName=7701e774ca2abe2e8050"

st.markdown(
    f"""
    <iframe src="{pbi_url}" 
            width="100%" 
            height="600" 
            frameborder="0" 
            allowFullScreen="true"></iframe>
    """, 
    unsafe_allow_html=True
)

st.components.v1.iframe(src=pbi_url, width=1000, height=700, scrolling=True)

# Conclusiones
st.markdown("## Conclusiones del Análisis")
st.markdown("""
---

### Principales Insights

1. **KPI de Puntuaciones:**
   - **Puntuación Promedio de Usuarios:** 4.18, logrando el objetivo mínimo establecido.
   - **Porcentaje de Buenas Puntuaciones:** Solo el 65.1% de los restaurantes alcanzan puntuaciones "buenas", por debajo del objetivo del 68%.
   - **Incremento en Reviews:** No se cumplió el objetivo, con un déficit del 89%.

2. **Tendencias de Puntuaciones:**
   - El promedio anual de puntuación muestra un ligero crecimiento, con una mayor pendiente entre 2022 y 2023.
   - A partir de 2024, el crecimiento se estabiliza levemente.

3. **Análisis de Ciudades para 2024:**
   - **Mejor puntuación promedio:** Malone.
   - **Peor puntuación promedio:** Ybor City.
   - **Ciudades con mayor cantidad de restaurantes:** Miami, Orlando y Jacksonville.
   - **Ciudades con menos restaurantes:** Lee, Jasper y Waldo.

4. **Análisis de Nichos (2022-2024):**
   - Top 5 ciudades con pocos restaurantes y puntuaciones excelentes: Bay Harbor Islands, Malone, Montverde, Seacrest y Shalimar.

5. **Distribución y Categorías:**
   - Los condados con mayor cantidad de restaurantes suelen tener puntuaciones promedio más altas.
   - Las categorías más populares en 2024 incluyen:
     - Restaurantes y Servicios.
     - Bares y Vida Nocturna.
     - Fast Food.
     - Cocina Caribeña y Latina.

6. **Oportunidades de Mercado:**
   - Las ciudades con pocos restaurantes y altas puntuaciones representan grandes oportunidades para expansión.
   - Las categorías populares son clave para identificar tendencias de mercado y áreas de enfoque estratégico.

---
""")

if st.button("Modelos", type ='tertiary',icon="➡️", use_container_width = True):
    
    st.switch_page("02_Asistente_de_predicción.py")