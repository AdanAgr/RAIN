import unittest
from DatasetLoader import *
from IU import *
from ModeloEntrenamiento import *
from ModeloSVD import *
from PersistenciaModelo import *
from Prediction import *
from Recommendation import *
from RecommendationSystem import *

class TestDatasetLoader(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para los tests."""
        self.loader = DatasetLoader()
        self.data_path = "./ml-10M"
    
    def test_cargar_datos_valid_file(self):
        """Verifica la carga de datos desde un archivo válido de ratings."""
        ratings = self.loader.cargar_datos(f"{self.data_path}/ratings.dat")
        
        # Verificar que el DataFrame no esté vacío
        self.assertFalse(ratings.empty)

        # Verificar que las columnas coincidan con las esperadas
        self.assertListEqual(list(ratings.columns), ['userId', 'movieId', 'rating', 'timestamp'])
    
    def test_cargar_peliculas_valid_file(self):
        """Verifica la carga de películas desde un archivo válido."""
        movies = self.loader.cargar_peliculas(self.data_path)
        
        # Verificar que el DataFrame no esté vacío
        self.assertFalse(movies.empty)

        # Verificar que las columnas coincidan con las esperadas
        self.assertListEqual(list(movies.columns), ['movieId', 'title', 'genres'])
    
    def test_cargar_tags_valid_file(self):
        """Verifica la carga de etiquetas desde un archivo válido."""
        tags = self.loader.cargar_tags(self.data_path)
        
        # Verificar que el DataFrame no esté vacío
        self.assertFalse(tags.empty)

        # Verificar que las columnas coincidan con las esperadas
        self.assertListEqual(list(tags.columns), ['userId', 'movieId', 'tag', 'timestamp'])
class TestRecommendationSystemSimple(unittest.TestCase):

    def test_recomendar(self):
        """Verifica que el sistema de recomendación funcione correctamente."""
        # Inicializar el sistema de recomendación
        recomendador = RecommendationSystem()

        # Cargar el modelo
        recomendador.cargar_modelo()

        resultado = recomendador.recomendar(
            generos=['Action'], decadas=["1990"], tags=['love', 'family'], top_n=5
        )

        self.assertNotEqual(resultado, [])
        
    def test_verificar_decada(self):
        year_test = None 
        """Verifica que el sistema de recomendación funcione correctamente."""
        # Inicializar el sistema de recomendación
        recomendador = RecommendationSystem()

        # Cargar el modelo
        recomendador.cargar_modelo()

        # Generar recomendaciones
        resultado = recomendador.recomendar(
            generos=['Action'], decadas=["1990"], tags=['love', 'family'], top_n=5
        )
        elemento1 = resultado[0]
        elemento1 = Recommendation.__str__(elemento1)
        year_test = Prediction.extraer_decada(elemento1)
        year_esperado = 1990
        # Verificar que el resultado coincida con el esperado
        self.assertEqual(year_esperado, year_test)   



class TestInterfaz(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test."""
        self.app = Interfaz()
        self.app.update_idletasks()

    def test_validate_id(self):
        """Verifica que la validación de ID funcione correctamente."""
        self.assertTrue(self.app.validate_id("12345"))  # ID válido
        self.assertFalse(self.app.validate_id("123456"))  # Más de 5 dígitos
        self.assertFalse(self.app.validate_id("abc"))  # Caracteres no numéricos

    def test_get_user_selection(self):
        """Verifica que la selección del usuario se almacene correctamente."""
        self.app.user_selection["generos"] = ["Action", "Comedy"]
        self.assertEqual(self.app.get_user_selection()["generos"], ["Action", "Comedy"])

    def test_get_user_text_tags(self):
        """Verifica que las etiquetas de texto se obtengan correctamente."""
        self.app.usertags = "love family friendship"
        self.assertEqual(self.app.get_user_text_tags(), ["love", "family", "friendship"])

    def tearDown(self):
        """Cierra la ventana después de cada test."""
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
