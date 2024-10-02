import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("peliculas.csv", sep=';', encoding='utf-8')

# Seleccionar el valor de la columna en la fila elegida

fila = 220
valor_columna = df.at[fila - 2, 'genres'] # Restamos 2 ya que el índice en Python empieza desde 0 y el archivo CSV tiene una fila de encabezado

print(f"Valor en la {fila}: {valor_columna}")
