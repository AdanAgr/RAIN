import pandas as pd
from surprise import Dataset, Reader
class DatasetLoader:
    def cargar_datos(self, ratings_filepath):
        # Cargar ratings
        ratings = pd.read_csv(ratings_filepath, sep='::', names=['userId', 'movieId', 'rating', 'timestamp'], engine='python')
        return ratings

    def crear_dataset_surprise(self, ratings):
        # Convertir el DataFrame de ratings a un conjunto de datos de Surprise
        reader = Reader(rating_scale=(0.5, 5))
        return Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
