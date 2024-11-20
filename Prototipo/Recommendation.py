class Recommendation:
    def __init__(self, title, predicted_rating):
        self.title = title
        self.predicted_rating = predicted_rating

    def __str__(self):
        """Devuelve una representación legible del objeto."""
        return f"{self.title}, Nota Estimada: {self.predicted_rating:.2f}\n"

    def display(self):
        return str(self)  
