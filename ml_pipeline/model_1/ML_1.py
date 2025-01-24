import streamlit as st
import pandas as pd
import folium
from sklearn.neighbors import KNeighborsRegressor
from streamlit_folium import st_folium

# Cargar los datos
@st.cache_data
def load_data():
    data = pd.read_csv(r'https://raw.githubusercontent.com/FrancoCavo/proyecto_final/refs/heads/ML_prediccion_puntajes/ML_1/restaurantes_2020.csv')
    return data

data = load_data()

# Entrenar el modelo KNN
@st.cache_resource
def train_knn(data):
    selected_data = data[['latitud', 'longitud', 'puntuacion_yelp']]
    X = selected_data[['latitud', 'longitud']]
    y = selected_data['puntuacion_yelp']
    
    knn_model = KNeighborsRegressor(n_neighbors=10, metric='manhattan', weights='distance')
    knn_model.fit(X, y)
    return knn_model

knn_model = train_knn(data)

# Función para predecir puntuación
def predict_score(model, lat, lon):
    new_data = pd.DataFrame([[lat, lon]], columns=['latitud', 'longitud'])
    predicted_score = model.predict(new_data)
    return predicted_score[0]

# Interfaz de Streamlit
st.title("Predicción de puntuación de restaurantes")
st.markdown("Ingrese las coordenadas para predecir la puntuación basada en el modelo KNN.")

# Entradas del usuario
lat = st.number_input("Latitud", value=27.8031, format="%.6f")
lon = st.number_input("Longitud", value=-82.7005, format="%.6f")

# Botón para predecir
if st.button("Predecir"):
    # Guardar la predicción en el estado de la sesión
    st.session_state['predicted_score'] = predict_score(knn_model, lat, lon)
    st.session_state['lat'] = lat
    st.session_state['lon'] = lon

# Mostrar resultados si ya se han calculado
if 'predicted_score' in st.session_state:
    score = st.session_state['predicted_score']
    lat = st.session_state['lat']
    lon = st.session_state['lon']

    st.success(f"Puntuación predicha: {score:.2f}")

    # Mapa interactivo
    st.markdown("### Mapa interactivo con la ubicación")
    mapa = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker(
        [lat, lon],
        popup=f"Latitud: {lat}<br>Longitud: {lon}<br>Puntuación: {score:.2f}",
        tooltip=f"Puntuación: {score:.2f}",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(mapa)

    st_folium(mapa, width=700, height=500)

