class Recommendation:
    def __init__(self, title, predicted_rating):
        self.title = title
        self.predicted_rating = predicted_rating

    def display(self):
        print(f"Película: {self.title}, Predicción de valoración: {self.predicted_rating:.2f}")
