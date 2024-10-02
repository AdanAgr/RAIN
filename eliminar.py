import pandas as pd
import ast

# Cargar el archivo CSV
df = pd.read_csv("peliculas.csv", sep=';', encoding='utf-8')

# Filtrar las filas donde:
# 'genres' no sea nulo y no esté vacío,
# 'keywords' no sea NaN,
# 'original_language' no sea nulo ni vacío,
# y las demás columnas no sean nulas o vacías.
df_filtrado = df[
    df['genres'].apply(lambda x: not pd.isna(x) and ast.literal_eval(x) != []) & 
    # df['keywords'].notna() &  Anot: Eliminada debido a que se cargaba 30000 instancias eliminando la mayoría de las filas
    df['original_language'].notna() &  # Filtrar donde 'original_language'
    (df['original_language'] != '') &    
    df['popularity'].notna() &           # Filtrar donde 'popularity'
    (df['popularity'] != '') &           
    df['production_companies'].notna() & # Filtrar donde 'production_companies'
    (df['production_companies'] != '[]') & 
    df['production_countries'].notna() &  # Filtrar donde 'production_countries'
    (df['production_countries'] != '[]') &  
    df['release_date'].notna() &          # Filtrar donde 'release_date'
    (df['release_date'] != '') &          
    df['runtime'].notna() &                # Filtrar donde 'runtime'
    (df['runtime'] != '') &                
    df['spoken_languages'].notna() &       # Filtrar donde 'spoken_languages'
    (df['spoken_languages'] != '[]') &     
    df['title'].notna() &                  # Filtrar donde 'title' 
    (df['title'] != '') &                  
    df['vote_average'].notna() &           # Filtrar donde 'vote_average' 
    (df['vote_average'] != '') &           
    df['vote_count'].notna() &             # Filtrar donde 'vote_count'
    (df['vote_count'] != '')               
]

# Guardar el nuevo DataFrame en un archivo CSV
df_filtrado.to_csv("testing.csv", sep=';', index=False, encoding='utf-8')

print(f"Filas después de eliminar nulos/vacíos: {len(df_filtrado)}")
