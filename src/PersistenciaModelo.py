import joblib

class PersistenciaModelo:
    def guardar_modelo(self, modelo, filename):
        joblib.dump(modelo, filename)
        print(f"Modelo guardado en {filename}")

    
