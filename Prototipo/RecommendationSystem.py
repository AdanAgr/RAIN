import joblib
from Prediction import Prediction

class RecommendationSystem:
    def __init__(self, model_filename='modelo_svd.pkl'):
        self.model_filename = model_filename
        self.model = None

    def cargar_modelo(self):
        self.model = joblib.load(self.model_filename)
        print(f"Modelo cargado desde {self.model_filename}")
        return self.model

    def recomendar(self, generos=None, decadas=None, tags=None,top_n=5):
        if not self.model:
            print("Modelo no cargado. Cargando el modelo...")
            self.cargar_modelo()

        recomendaciones = Prediction(self.model).recomendar_peliculas(generos=generos, decadas=decadas, tags=tags,top_n=top_n)
        return recomendaciones

if __name__ == "__main__":
    recomendacion = RecommendationSystem()
    print("Recomendación 1:")
    recomendacion.recomendar(generos=["Romance", "Drama","Thriller"], decadas=[1980, 1990], tags=["sex"],top_n=5)
    print("Recomendación 2:")
    recomendacion.recomendar(generos=["Comedy", "Western"], decadas=[1990, 2000], tags=["wizard"],top_n=5)

