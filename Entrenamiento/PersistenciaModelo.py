import joblib

class PersistenciaModelo:
    def guardar_modelo(self, modelo, filename):
        joblib.dump(modelo, filename)
        print(f"Modelo guardado en {filename}")

    def cargar_modelo(self, filename):
        modelo = joblib.load(filename)
        print(f"Modelo cargado desde {filename}")
        return modelo
