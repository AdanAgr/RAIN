from Recommendation import Recommendation

class Model:
    def predict(self, inputData):
        content = f"Recommended based on input: {inputData}"
        return Recommendation(content)