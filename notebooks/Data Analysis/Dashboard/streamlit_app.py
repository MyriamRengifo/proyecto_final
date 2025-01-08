import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título del dashboard
st.title("Dashboard de Prueba - Demo2")

# url 
pwbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiZGQwOGY4NDMtOWMzNi00YjU0LWFjZWUtNTlkOWU2ODFiODQ1IiwidCI6IjljNWM4NjYyLTFiZjUtNGU5NC1hODIwLTVlM2NhMTI2Zjc1MiIsImMiOjR9'


st.markdown(
    f"""
    <iframe src="{pwbi_url}" 
            width="100%" 
            height="600" 
            frameborder="0" 
            allowFullScreen="true"></iframe>
    """, 
    unsafe_allow_html=True
)