from surprise import SVD, accuracy
from surprise.model_selection import train_test_split

class ModeloSVD:
    def __init__(self):
        self.model = SVD()

    def entrenar(self, data):
        trainset, testset = train_test_split(data, test_size=0.2)
        self.model.fit(trainset)

        predictions = self.model.test(testset)
        rmse = accuracy.rmse(predictions)
        mae = accuracy.mae(predictions)

        return self.model