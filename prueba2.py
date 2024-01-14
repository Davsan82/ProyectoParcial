import json
import zipfile
import os
import opendatasets as od
import pandas as pd
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi

api_token = {"username":"davidsanchezcalle","key":"808d7b5385b3285eb256b2161df70724"}

##Contectar a Kaggle
api_token = {"username":"davidsanchezcalle","key":"808d7b5385b3285eb256b2161df70724"}

##Contectar a Kaggle

with open("C:/Users/a0197/.kaggle/kaggle.json","w") as file:
    json.dump(api_token, file)

location = "C:/pparcial/dataset"

# Configura la ruta hacia tu archivo JSON de credenciales
os.environ['KAGGLE_CONFIG_DIR'] = 'C:/Users/a0197/.kaggle/kaggle.json'  # Reemplaza con la ruta correcta

# Nombre del dataset que deseas descargar desde Kaggle
dataset_name = 'davidsanchezcalle/starbucks' # Reemplaza con tu nombre de usuario y nombre del dataset

# Inicializa la API de Kaggle
api = KaggleApi()
api.authenticate()

# Descarga el dataset como un archivo ZIP
api.dataset_download_files(dataset_name, unzip=True)  # Descarga y descomprime el archivo ZIP

# Nombre del archivo ZIP descargado
nombre_archivo_zip = 'nombre_del_archivo.zip' 

# Extrae el archivo CSV del ZIP
with ZipFile(nombre_archivo_zip, 'r') as zip_ref:
    # Encuentra el nombre del archivo CSV dentro del ZIP (puede variar según el dataset)
    for file_name in zip_ref.namelist():
        if file_name.endswith('.csv'):
            zip_ref.extract(file_name, '/ruta/hacia/donde/guardar')  # Reemplaza con la ruta donde quieres guardar el CSV
            print(f"{file_name} extraído con éxito.")
            break  # Una vez encontrado y extraído el archivo CSV, detiene el bucle
