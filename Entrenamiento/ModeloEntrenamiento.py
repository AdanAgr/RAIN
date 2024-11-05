from ModeloSVD import ModeloSVD
from DatasetLoader import DatasetLoader
from PersistenciaModelo import PersistenciaModelo

class ModeloEntrenamiento:
    
    def cargar_datos(self, ratings_filepath):
        # Cargar los datos de ratings
        loader = DatasetLoader()
        ratings = loader.cargar_datos(ratings_filepath)
        return loader.crear_dataset_surprise(ratings)

    def entrenarModelo(self, data):
        # Dividir los datos y entrenar el modelo
        model = ModeloSVD().entrenar(data)
        return model

    def guardarModelo(self, modelo, path):
        PersistenciaModelo().guardar_modelo(modelo, path)

if __name__ == "__main__":

    ratings_filepath = '/home/rial/Surprise/Código UwU/ml-10M/ratings.dat'

    modelo_entrenamiento = ModeloEntrenamiento()
    dataset = modelo_entrenamiento.cargar_datos(ratings_filepath)

    modelo = modelo_entrenamiento.entrenarModelo(dataset)

    modelo_entrenamiento.guardarModelo(modelo, 'modelo_svd.pkl')