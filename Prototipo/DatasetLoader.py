import pandas as pd
from surprise import Dataset, Reader
class DatasetLoader:

    def cargar_datos(self, ratings_path):
        ratings = pd.read_csv(ratings_path, sep='::', names=['userId', 'movieId', 'rating', 'timestamp'], engine='python')
        return ratings

    def cargar_peliculas(self, data_path):
        movies_file = f'{data_path}/movies.dat'
        movies_df = pd.read_csv(movies_file, sep='::', engine='python', names=['movieId', 'title', 'genres'])
        return movies_df

    def cargar_tags(self, data_path):
        """Carga las etiquetas de las películas como un DataFrame sin agrupar."""
        tags_file = f'{data_path}/tags.dat'
        tags = pd.read_csv(tags_file, sep='::', engine='python', names=['userId', 'movieId', 'tag', 'timestamp'])
        return tags

    def crear_dataset_surprise(self, ratings):
        reader = Reader(rating_scale=(0.5, 5))
        return Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
