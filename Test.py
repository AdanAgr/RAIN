import unittest
from Entrenamiento import cargar_data

class TestCargarData(unittest.TestCase):
    def test_load_valid_dat_file(self):
        # Llamar a la función cargar_data con el archivo de datos
        data = cargar_data('movies')
        
        # Verificar que el DataFrame no esté vacío
        self.assertFalse(data.empty)
        
        # Verificar que las columnas coincidan con las esperadas
        self.assertEqual(list(data.columns), ['movie_id', 'title', 'genres'])

if __name__ == '__main__':
    unittest.main()
