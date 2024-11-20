from surprise import SVD, accuracy
from surprise.model_selection import train_test_split, GridSearchCV

class ModeloSVD:
    def __init__(self, params=None):
        self.model = SVD(**params) if params else SVD()

    def entrenar(self, data):
        trainset, testset = train_test_split(data, test_size=0.2)
        self.model.fit(trainset)

        predictions = self.model.test(testset)
        rmse = accuracy.rmse(predictions)
        mae = accuracy.mae(predictions)

        return self.model, rmse, mae

    def optimizar_parametros(self, data):
        param_grid = {
            'n_factors': [50],
            'n_epochs': [20, 30],
            'lr_all': [0.002],
            'reg_all': [0.02, 0.1]
        }

        gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)
        gs.fit(data)

        best_params = gs.best_params['rmse']
        print("Mejores parámetros:", best_params)
        print("Mejor RMSE:", gs.best_score['rmse'])

        # Actualiza el modelo con los mejores parámetros
        self.model = SVD(**best_params)
        return best_params