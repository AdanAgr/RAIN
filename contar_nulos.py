# Descripción: Contar la cantidad de valores nulos y vacíos en un archivo CSV.
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("peliculas.csv", sep=';', encoding='utf-8')

# Listar las columnas a analizar
columnas = [
    'keywords',
    'genres',
    'original_language',
    'original_title',
    'overview', 
    'popularity', 
    'production_companies', 
    'production_countries', 
    'release_date', 
    'runtime', 
    'spoken_languages', 
    'title', 
    'vote_average', 
    'vote_count'
]

# Contar nulos y vacíos para cada columna
for columna in columnas:
    vacios = (df[columna] == '[]').sum()  # Contar cadenas vacías
    nulos = df[columna].isna().sum()    # Contar NaN
    print(f"Cantidad de valores vacíos en la columna '{columna}': {vacios}")
    print(f"Cantidad de valores nulos en la columna '{columna}': {nulos}")
