import pandas as pd
from Recommendation import Recommendation
from DatasetLoader import DatasetLoader

class Prediction:
    def __init__(self, model):
        self.model = model
        data_path = "/home/rial/Surprise/Código UwU/ml-10M"
        self.movies_data = DatasetLoader().cargar_peliculas(data_path)

    def filtrar_peliculas(self, generos=None, decadas=None):
        peliculas_filtradas = self.movies_data

        # Filtrar por géneros
        if generos:
            filtro_generos = pd.Series([True] * len(peliculas_filtradas))
            for genero in generos:
                filtro_generos &= peliculas_filtradas['genres'].str.contains(genero, case=False, na=False)
            peliculas_filtradas = peliculas_filtradas[filtro_generos]

        # Filtrar por décadas
        if decadas:
            peliculas_filtradas = peliculas_filtradas[peliculas_filtradas['title'].apply(
                lambda title: self.extraer_decada(title) in decadas
            )]

        return dict(zip(peliculas_filtradas['movieId'], peliculas_filtradas['title']))

    @staticmethod
    def extraer_decada(titulo):
        import re
        match = re.search(r'\((\d{4})\)', titulo)
        if match:
            year = int(match.group(1))
            return (year // 10) * 10
        return None

    def recomendar_peliculas(self, generos=None, decadas=None, top_n=5):
        peliculas_filtradas = self.filtrar_peliculas(generos=generos, decadas=decadas)
        
        predictions = []
        for movie_id, title in peliculas_filtradas.items():
            user_id = 999999  # ID de usuario ficticio
            predicted_rating = self.model.predict(user_id, movie_id).est
            recommendations = Recommendation(title, predicted_rating)
            predictions.append(recommendations)

        # Ordenar y obtener el top N de recomendaciones
        top_recommendations = sorted(predictions, key=lambda x: x.predicted_rating, reverse=True)[:top_n]

        # Mostrar las recomendaciones en pantalla
        for recommendation in top_recommendations:
            recommendation.display()

        return top_recommendations
