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

    def recomendar(self, generos=None, decadas=None, top_n=5):
        if not self.model:
            print("Modelo no cargado. Cargando el modelo...")
            self.cargar_modelo()

        # Pasar el modelo a la instancia de Prediction
        recomendaciones = Prediction(self.model).recomendar_peliculas(generos=generos, decadas=decadas, top_n=top_n)
        return recomendaciones

if __name__ == "__main__":
    recomendacion = RecommendationSystem()
    recomendacion.recomendar(generos=["Drama"], decadas=[1950], top_n=5)
