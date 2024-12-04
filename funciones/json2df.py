import json
import pandas as pd

def json2df(ruta):
    """
    Carga un archivo JSON línea por línea y lo convierte en un DataFrame.
    
    parámetro entrada: Ruta al archivo JSON.
    return: DataFrame con los datos del archivo JSON.
    """
    with open(ruta, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]
    
    return pd.DataFrame(data)

def multiple_json2df(rutas):
    """
    Carga múltiples archivos JSON y los convierte en un solo DataFrame.
    
    parámetro entrada: Lista de rutas a los archivos JSON.
    return: DataFrame con los datos de todos los archivos JSON combinados.
    """
    all_data = []
    
    for ruta in rutas:
        with open(ruta, 'r', encoding='utf-8') as f:
            all_data.extend([json.loads(line) for line in f])
    
    return pd.DataFrame(all_data)
