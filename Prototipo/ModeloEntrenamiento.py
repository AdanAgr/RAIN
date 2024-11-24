from ModeloSVD import ModeloSVD
from DatasetLoader import DatasetLoader
from PersistenciaModelo import PersistenciaModelo

class ModeloEntrenamiento:
    
    def cargar_datos(self, ratings_path):
        loader = DatasetLoader()
        ratings = loader.cargar_datos(ratings_path)
        return loader.crear_dataset_surprise(ratings)

    def entrenarModelo(self, data, optimizar=False):
        modelo_svd = ModeloSVD()

        if optimizar:
            mejores_parametros = modelo_svd.optimizar_parametros(data)
            print(f"Mejores parámetros encontrados: {mejores_parametros}")

        model, rmse, mae = modelo_svd.entrenar(data)
        print(f"RMSE del modelo entrenado: {rmse}, MAE: {mae}")
        return model

    def guardarModelo(self, modelo, path):
        PersistenciaModelo().guardar_modelo(modelo, path)

if __name__ == "__main__":
    ratings_path = '/home/rial/Surprise/Prototipo/ml-10M/ratings.dat'

    modelo_entrenamiento = ModeloEntrenamiento()
    dataset = modelo_entrenamiento.cargar_datos(ratings_path)

    modelo = modelo_entrenamiento.entrenarModelo(dataset, optimizar=False)

    modelo_entrenamiento.guardarModelo(modelo, 'modelo_svd.pkl')
