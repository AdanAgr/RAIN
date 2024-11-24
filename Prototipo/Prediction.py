import pandas as pd
from Recommendation import Recommendation
from DatasetLoader import DatasetLoader
from tkinter import messagebox
class Prediction:
    def __init__(self, model):
        self.model = model
        data_path = "./ml-10M"
        self.movies_data = DatasetLoader().cargar_peliculas(data_path)
        self.tags_data = DatasetLoader().cargar_tags(data_path)  

    def filtrar_peliculas(self, generos=None, decadas=None, tags=None):
        peliculas_filtradas = self.movies_data

        # Filtrar por tags
        if tags:
            filtro_tags = self.tags_data[self.tags_data['tag'].str.contains('|'.join(tags), case=False, na=False)]
            movie_ids_con_tags = set(filtro_tags['movieId'])
            peliculas_filtradas = peliculas_filtradas[peliculas_filtradas['movieId'].isin(movie_ids_con_tags)]

        # Filtrar por décadas
        if decadas:
            peliculas_filtradas = peliculas_filtradas[peliculas_filtradas['title'].apply(
                lambda title: self.extraer_decada(title) in [int(decada) for decada in decadas]
            )]

        # Filtrar por géneros
        if generos:
            peliculas_filtradas = peliculas_filtradas.reset_index(drop=True)  # Reiniciar índices
            filtro_and = pd.Series([True] * len(peliculas_filtradas))  # Generar filtro booleano actualizado
            for genero in generos:
                filtro_and &= peliculas_filtradas['genres'].str.contains(genero, case=False, na=False)
            
            peliculas_filtradas_and = peliculas_filtradas[filtro_and]

            # Si no hay resultados en el filtro AND, usar OR como fallback
            if peliculas_filtradas_and.empty:
                messagebox.showwarning("Aviso","No se han encontrado películas que contengan todos los géneros ajustados. Usando filtro Or.")
                filtro_or = pd.Series([False] * len(peliculas_filtradas))
                for genero in generos:
                    filtro_or |= peliculas_filtradas['genres'].str.contains(genero, case=False, na=False)
                peliculas_filtradas = peliculas_filtradas[filtro_or]
            else:
                peliculas_filtradas = peliculas_filtradas_and

        if peliculas_filtradas.empty:
            messagebox.showwarning("Aviso","No se han encontrado películas para estas especificaciones, aquí tiene una lista de películas que creemos le gustarán:")
            peliculas_filtradas = self.movies_data
            return dict(zip(peliculas_filtradas['movieId'], peliculas_filtradas['title']))
        else:
            return dict(zip(peliculas_filtradas['movieId'], peliculas_filtradas['title']))


    @staticmethod
    def extraer_decada(titulo):
        import re
        match = re.search(r'\((\d{4})\)', titulo)
        if match:
            year = int(match.group(1))
            return (year // 10) * 10
        return None

    def recomendar_peliculas(self, user=None, generos=None, decadas=None, tags=None,top_n=5):
        peliculas_filtradas = self.filtrar_peliculas(generos=generos, decadas=decadas,tags=tags)
        
        predictions = []
        for movie_id, title in peliculas_filtradas.items():
            user_id = user  
            predicted_rating = self.model.predict(user_id, movie_id).est
            recommendations = Recommendation(title, predicted_rating)
            predictions.append(recommendations)

        top_recommendations = sorted(predictions, key=lambda x: x.predicted_rating, reverse=True)[:top_n]

        for recommendation in top_recommendations:
            recommendation.display()

        return top_recommendations
