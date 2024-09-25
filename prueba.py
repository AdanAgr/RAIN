import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('movies.csv')

# Obtener el valor de 'release_date' en el índice 10
release_date = df.loc[10, 'release_date']

print(f'El release_date del elemento en el índice 10 es: {release_date}')
