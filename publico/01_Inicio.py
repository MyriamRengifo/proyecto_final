import streamlit as st
st.set_page_config(
        page_title="Principal",
        page_icon=":material/favorite:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
#st.sidebar.page_link("pages/02_asistente_de_prediccion.py", label="Your Models")


st.markdown("# [Titulo del proyecto]")
st.markdown("## [Titulo del dashboard]")

st.markdown("""
            -------
            [introduccióm]
            -------
            """)

st.markdown("""
            [Texto complementario]
            """)

pbi_url = "https://app.powerbi.com/view?r=eyJrIjoiMDQ4MTRiZjMtMzA2ZS00MTEwLThhM2QtMmFmMzBkMjkzZjA0IiwidCI6IjljNWM4NjYyLTFiZjUtNGU5NC1hODIwLTVlM2NhMTI2Zjc1MiIsImMiOjR9&pageName=455fbd065761d7b4d03f"

st.components.v1.iframe(src=pbi_url, width=1000, height=700, scrolling=True)

st.markdown("## [SubTitulo para conclusiones]")

st.markdown("""
            -------
            [insights]
            -------
            """)

st.markdown("""
            [Texto complementario]
            """)

if st.button("Modelos", type ='secondary',icon="➡️", use_container_width = True):
    
    st.switch_page("pages/02_asistente_de_prediccion.py")