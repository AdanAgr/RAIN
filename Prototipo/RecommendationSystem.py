import joblib
from Prediction import Prediction
class RecommendationSystem:
    def __init__(self, model_filename='modelo_svd.pkl'):
        self.model_filename = model_filename
        self.model = None

    def cargar_modelo(self):
        print("Cargando modelo...")
        self.model = joblib.load(self.model_filename)
        print(f"Modelo cargado desde {self.model_filename}")
        return self.model

    def recomendar(self, user=None,generos=None, decadas=None, tags=None,top_n=5):
        if not self.model:
            print("Modelo no cargado. Cargando el modelo...")
            self.cargar_modelo()

        recomendaciones = Prediction(self.model).recomendar_peliculas(user=user,generos=generos, decadas=decadas, tags=tags,top_n=top_n)
        return recomendaciones

if __name__ == "__main__":
    recomendador = RecommendationSystem()
    recomendador.cargar_modelo()
    print(recomendador.recomendar(generos=['Action'], decadas=["1990"], tags=['love', 'family'], top_n=5))

