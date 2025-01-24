import streamlit as st
from streamlit_folium import st_folium 
import folium

import pandas as pd
from typing import Literal

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import GMF

cols = {
    'id': "id_nombre",
    'nombre': 'nombre',
    'id_ciudad': "id_ciudad",
    'nombre_ciudad': "ciudad",
    'latitud': "latitud", 
    'longitud': "longitud", 
    'puntuacion': "puntuacion_usuarios",
    'categories': "categorias",
    'año': "año"
}

#?region functions
# Cargar los datos
@st.cache_data
def load_yearly():
    yearly = pd.read_parquet(r'https://github.com/JorgeLuisSR/testing_streamlit_discardable/raw/refs/heads/main/Datasets/florida_yearly.parquet')
    return yearly

@st.cache_data
def load_restaurants():
    restaurants = pd.read_parquet('https://github.com/JorgeLuisSR/testing_streamlit_discardable/raw/refs/heads/main/Datasets/florida_restaurants.parquet')
    return restaurants

@st.cache_data
def load_forecaster():
    forecaster = GMF.GrandMeansForecaster(degree=5)
    return forecaster

@st.cache_resource
def train_knn():
    selected_data = restaurants[[cols["latitud"], cols["longitud"], cols["puntuacion"]]]
    X = selected_data[[cols["latitud"], cols["longitud"]]]
    y = selected_data[cols["puntuacion"]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    best_knn_model = KNeighborsRegressor(n_neighbors=10, metric='manhattan', weights='distance')
    fitted = best_knn_model.fit(X_train, y_train)
    return fitted

def is_viable_rest(row) -> bool:
    target_data = yearly[yearly[cols["id"]] == row[cols["id"]]]
    target_data = target_data[[cols["año"], cols["puntuacion"]]]
    # Verificar si hay datos suficientes
    return (len(target_data) > 1)

def is_viable_cat(cat, city):
    target_data = yearly[yearly[cols['id_ciudad']] == city]
    target_data = target_data[target_data[cols["categories"]].str.contains(cat)]
    
    return (len(target_data) > 1)


def tendency_restaurant(id_nombre, year:int=2023):#, *, target:Literal["puntuacion_usuarios", "puntuacion_yelp"]="puntuacion_usuarios")-> None | list[float]:
    """
    Predict the tendency in the public opinion of a restaurant 
    identified by a local ``id_nombre`` for the ``year`` using the 
    ``target`` column.

    Parameters
    ----------
    id_nombre : int
        The id in the local parquet dataframes
        
        If id is not ``ìnt`` it may not return expected entries.
    year : int
        Current year or next in the dataset.
        
        Big time gaps between data samples may lead to extreme predictions.
    target : "puntuacion_usuarios" or "puntuacion_yelp"
        Whether to use the scores from google or yelp

    Returns
    ----------
    None : if the dataset has less than 2 entries for the restaurant identified 
        by ``id_nombre``.
    list: [float a, float b]
        being a the predicted value of the model and b the diference between the 
        predicted year an the previous year

        If the previous year is not part of the dataset the value will be predicted 
        for the previous year and then used to obtain b

    See Also
    --------
    sklearn.preprocessing.PolynomialFeatures
    sklearn.linear_model.LinearRegression
    sklearn.pipeline 

    Example
    --------

    >>> tendency_restaurant(0, 2021)
    [3.9482100661844015, 0.4482100661844015]
    >>> tendency_restaurant(0, target="puntuacion_yelp")
    [3.0, 0.0]

    """

    target_data = yearly[yearly[cols["id"]] == id_nombre]
    target_data = target_data[[cols["año"], cols["puntuacion"]]]
    # Verificar si hay datos suficientes
    if len(target_data) < 2:
        return

    target_data.sort_values(by=cols['año'], inplace=True)
    data = {
        "año": target_data[cols['año']].values,
        "value": target_data[cols["puntuacion"]].values
    }
    df = pd.DataFrame(data)

    predicted_value = forecaster.fit_predict(df, year)
    # print(f"Predicted value for {year}: {predicted_value[0]:.2f}, for a difference of {predicted_value[1]:.2f}")

    return predicted_value

def tendency_category(category: str, city_parquet_id: int | None = None, year:int=2023):#, *, target:Literal["puntuacion_usuarios", "puntuacion_yelp"]="puntuacion_usuarios")-> None | list[float]:
    """
    Predict the tendency in the mean of the public opinion of a ``category`` 
    of restaurants in the city identified by  ``city_parquet_id`` for the 
    ``year`` using the ``target`` column.

    Parameters
    ----------
    category : str
        The category of restaurant registered in the local parquet dataframes.
        
        Note that category is case-sensitive.
    city_parquet_id : int or None
        The local id for the cities registered in the local parquet dataframes
        used to give more relevant answers to an area.

        If id is ´´´None´´ predictions will be made with the mean of all cities.
    year : int
        current year or next in the dataset.
        
        Big time gaps between data samples may lead to extreme predictions.
    target : "puntuacion_usuarios" or "puntuacion_yelp"
        Whether to use the scores from google or yelp.
    
    Returns
    ----------
    None : if the dataset has less than 2 entries from different years for the category 
        identified by ``category``.
    list: [float a, float b]
        being a the predicted value of the model and b the diference between the 
        predicted year an the previous year

        If the previous year is not part of the dataset the value will be predicted 
        for the previous year and then used to obtain b

    See Also
    --------
    sklearn.preprocessing.PolynomialFeatures
    sklearn.linear_model.LinearRegression
    sklearn.pipeline 

    Example
    --------

    >>> tendency_category("Bars", 20, 2023)
    [3.8271445697173476, -0.04645543028265209]
    >>> tendency_category("Bars", 20, 2023, target="puntuacion_yelp")
    [4.027870584279299, 0.07067058427929895]

    """

    if city_parquet_id is not None:
        target_data = yearly[yearly[cols['id_ciudad']] == city_parquet_id]
        target_data = target_data[target_data[cols["categories"]].str.contains(category)]
    else:
        target_data = yearly[yearly[cols["categories"]].str.lower().contains(category.lower())]
        
    target_data = target_data[[cols["año"], cols["puntuacion"]]]
    
    # Agrupar por año y calcular la puntuación promedio de todos los restaurantes
    target_data = target_data.groupby(cols["año"])[cols["puntuacion"]].mean().reset_index()
    
    # Verificar si hay datos suficientes
    if len(target_data) < 2:
        return
        # print("No hay suficientes datos para hacer un pronóstico.") #! Remove on deployment

    target_data.sort_values(by=cols["año"], inplace=True)
    data = {
        "año": target_data[cols["año"]].values,
        "value": target_data[cols["puntuacion"]].values
    }
    df = pd.DataFrame(data)

    predicted_value = forecaster.fit_predict(df, year)
    # print(f"Predicted value for {year}: {predicted_value[0]:.2f}, for a difference of {predicted_value[1]:.2f}")

    return predicted_value

def hay_suficientes_restaurantes(latitud, longitud):
    """Función para verificar si hay al menos 10 restaurantes en un radio de 1000 metros"""
    radio = 0.018  # Aproximadamente 1000 metros en grados de latitud/longitud
    restaurantes_cercanos = restaurants[
        (restaurants[cols["latitud"]] >= latitud - radio) & (restaurants[cols["latitud"]] <= latitud + radio) &
        (restaurants[cols["longitud"]] >= longitud - radio) & (restaurants[cols["longitud"]] <= longitud + radio)
    ]
    return len(restaurantes_cercanos) >= 10, restaurantes_cercanos

def predecir_puntaje(latitud, longitud):
    """Función para predecir el puntaje basado en latitud y longitud"""
    hay_restaurantes, restaurantes_cercanos = hay_suficientes_restaurantes(latitud, longitud)
    if hay_restaurantes:
        nuevo_dato = pd.DataFrame([[latitud, longitud]], columns=[cols["latitud"], cols["longitud"]])
        puntaje_predicho = best_knn_model.predict(nuevo_dato)
        return puntaje_predicho[0], restaurantes_cercanos
    else:
        return None, restaurantes_cercanos

#endregion

forecaster = load_forecaster()
yearly = load_yearly()
restaurants = load_restaurants()
best_knn_model = train_knn()

# Interfaz de Streamlit
st.title("Predicción de puntuación de restaurantes")

st.markdown("**Antes que nada!** \n\n Haz clic en el mapa para seleccionar un punto en Florida sobre el que te interese obtener más información, será sobre los alrededores del punto de interes que se desarrollarán los modelos.")
# Crear dos columnas para el diseño
col1, col2 = st.columns([0.45, 0.45], vertical_alignment = "center")


with col1:
    # Crear un mapa centrado en Florida
    st.markdown("**Mapa de seleccion de ubicación**")
    m = folium.Map(location=[27.994402, -81.760254], zoom_start=7)
    # Habilitar clics para agregar marcadores
    folium.ClickForMarker().add_to(m, "selected", 0)
    # Mostrar el mapa en Streamlit
    output = st_folium(m, width=300, height=200)

with col2:
    
    st.markdown("**Restaurantes cercanos:**")
    # """
    # if output['last_clicked']:
    #     st.write("#### Resultados")
    #     st.write(f"Latitud: {latitud:.6f}")
    #     st.write(f"Longitud: {longitud:.6f}")

    #     # Realizar la predicción y mostrar el resultado
    #     st.write("#### " + resultado)
    # """

    # Mostrar el mapa con marcadores de restaurantes cercanos si existen
    if output['last_clicked']:
        latitud = output['last_clicked']['lat']
        longitud = output['last_clicked']['lng']
        st.session_state["resultado"], st.session_state["restaurantes_cercanos"] = predecir_puntaje(latitud, longitud)
        if st.session_state["restaurantes_cercanos"] is not None:
            if st.session_state["resultado"] is not None:
            # st.write("### Restaurantes cercanos")
                mapa_resultado = folium.Map(location=[latitud, longitud], zoom_start=13)

                # Agregar marcadores para restaurantes cercanos
                for _, row in st.session_state["restaurantes_cercanos"].iterrows():
                    folium.Marker(
                        [row[cols['latitud']], row[cols["longitud"]]],
                        popup=f"<b>Restaurante: </b><br>{row[cols['nombre']]}<br>Puntaje: {row[cols['puntuacion']]}",
                        icon=folium.Icon(color='blue')
                    ).add_to(mapa_resultado)

                # Agregar marcador para la ubicación seleccionada
                folium.Marker(
                    [latitud, longitud],
                    popup=f"<b>Ubicación seleccionada</b><br>Latitud: {latitud}<br>Longitud: {longitud}",
                    icon=folium.Icon(color='green')
                ).add_to(mapa_resultado)

                # Mostrar el mapa actualizado
                st_folium(mapa_resultado, width=300, height=200)
            else:
                st.warning("No hay suficientes restaurantes en esta area, pruebe con otra ubicación")

if "resultado" in st.session_state and st.session_state["resultado"] is not None:
    st.success(f"**El puntaje esperado en esta zona es de _{st.session_state['resultado']:.2f}_**", icon="⭐")
    st.info("El puntaje esperado es un indicativo del puntaje necesario para poder competir con los restaurantes de la zona. \n Tambien es una medida util para estimar la puntuación que podriamos esperar de poner un restaurante en esta area.", icon="📝")


st.markdown("### predecir puntajes para el siguiente año:")

st.markdown("""<b>
            A la hora de invertir en un restaurante es util obtener un estimativo del valor de su opinión pública para el futuro.
            Por este motivo el siguiente modelo le asistirá en la predición de la puntuación de los usuarios según
            los restaurantes seleccionados previamente en el <i style='color:red;'>mapa superior</i>, y sus categorias.
            </b>""", unsafe_allow_html=True)

labeling ,subcol1, subcol2, subcol3,_ = st.columns([0.21, 0.18, 0.1, 0.18, 0.3], vertical_alignment='center')
with labeling:
    st.write("modo de predicción:")
with subcol2:
    st.toggle(label="restaurante o categoria", label_visibility="collapsed", key="see_rest")
with subcol1:
    if st.session_state["see_rest"]:
        st.html('<p style="opacity: .2;"><small>predecir por</small> categoria</p>')
    else:
        st.html('<p style="opacity: 1;color:orange;"><small>predecir por</small> <b>categoria</b></p>')
with subcol3:
    if st.session_state["see_rest"]:
        st.html('<p style="opacity: 1;color:orange;"><small>predecir por</small> <b>restaurante</b></p>')
    else:
        st.html('<p style="opacity: .2;"><small>predecir por</small> restaurante</p>')

# else:
#     city = st.number_input(label="ID de la ciudad",value=None, step=1, key="id_ciudad",placeholder="especificar la ciudad")

col3, col4 = st.columns(2,vertical_alignment='center')

# Entradas del usuario
with col3:
    if "restaurantes_cercanos" in st.session_state:
        if st.session_state["see_rest"]:
            if st.session_state["restaurantes_cercanos"] is not None and len(st.session_state["restaurantes_cercanos"])>0:
                #st.write(st.session_state["restaurantes_cercanos"])
                validity_df = pd.DataFrame(st.session_state["restaurantes_cercanos"]).apply(is_viable_rest, axis=1)
                if len(st.session_state["restaurantes_cercanos"][validity_df])>0:
                    option = st.selectbox(
                        "predecir sobre el restaurante...",
                        st.session_state["restaurantes_cercanos"][validity_df][[cols["nombre"]]],
                        key="last_restaurant_name"
                    )
                    st.session_state["last_restaurant_id"] = int(st.session_state["restaurantes_cercanos"].loc[st.session_state["restaurantes_cercanos"][cols["nombre"]]==st.session_state["last_restaurant_name"], cols["id"]].iloc[0])
                else: 
                    st.warning("No hay resultados disponibles para predicción en esta area", icon="😔")
                    st.info("**Que Significa esto?** \n\n Es posible que en el area seleccionada no hayan restaurantes que tengan datos historicos en nuestras bases de datos. \n\n Lo que puede indicar que los restaurantes en el area son muy nuevos.", icon="❓")
                # st.write(st.session_state["last_restaurant_id"], restaurantes_cercanos.loc[restaurantes_cercanos[cols["nombre"]]==st.session_state["last_restaurant_name"], cols["id"]])
        else:
            if st.session_state["restaurantes_cercanos"] is not None and len(st.session_state["restaurantes_cercanos"])>0:
                st.session_state["city"] = st.session_state["restaurantes_cercanos"][cols["id_ciudad"]].mode()[0]

                seudocategorias = list()
                for _, row in st.session_state["restaurantes_cercanos"].iterrows():
                    cats = str(row[cols["categories"]])
                    for c in cats.split(","):
                        if c.strip(" ['] ") not in seudocategorias:
                            seudocategorias.append(c.strip(" ['] "))
                
                validity_df = [is_viable_cat(x, st.session_state["city"]) for x in seudocategorias]

                st.session_state["categories"] = list()
                for i, c in enumerate(seudocategorias):
                    if validity_df[i]:
                        st.session_state["categories"].append(c)

                if len(st.session_state["categories"])>0:
                    option = st.selectbox(
                        "predecir sobre la categoria...",
                        st.session_state["categories"],
                        key="last_category")
                else: 
                    st.warning("No hay resultados disponibles para predicción en esta area", icon="😔")
                    st.info("**Que Significa esto?** \n\n Es posible que en el area seleccionada no hayan restaurantes que tengan datos historicos en nuestras bases de datos. \n\n Lo que puede indicar que los restaurantes en el area son muy nuevos.", icon="❓")

                # st.write(st.session_state["last_category"])
                
            # st.write(st.session_state["city"])
        
        # Botón para predecir
        if st.button("Predecir", type ='primary',icon="🔎", use_container_width = True):
            # Guardar la predicción en el estado de la sesión
            if 'last_restaurant_id' in st.session_state:
                if st.session_state["see_rest"]:
                    st.session_state['gmf_score'] = tendency_restaurant(st.session_state['last_restaurant_id'])
            
            if 'last_category' in st.session_state and 'city' in st.session_state:
                if not st.session_state["see_rest"]:
                    st.session_state['gmf_score'] = tendency_category( st.session_state['last_category'], st.session_state["city"])

with col4:
    # Mostrar resultados si ya se han calculado
    if 'gmf_score' in st.session_state:
        predicted_value = st.session_state['gmf_score']
        if predicted_value is None:
            st.warning(f"No hay suficientes registros historicos que cumplan las condiciones especificadas.\n\n intente otra vez con otra configuración")
        else:
            st.success(f"Para el año 2023 se predice una puntuación de: **{predicted_value[0]:.2f}**. \n\n Siendo **{predicted_value[1]:.2f}** puntos en relación al año anterior")


if st.button("Modelos", type ='secondary',icon="⬅️", use_container_width = True):
    st.switch_page("01_Inicio.py")