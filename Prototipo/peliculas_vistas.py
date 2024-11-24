import pandas as pd

data_path = "/home/rial/Surprise/Prototipo/ml-10M"

ratings_file = f'{data_path}/ratings.dat'
ratings = pd.read_csv(ratings_file, sep='::', engine='python', names=['userId', 'movieId', 'rating', 'timestamp'])

movies_file = f'{data_path}/movies.dat'
movies = pd.read_csv(movies_file, sep='::', engine='python', names=['movieId', 'title', 'genres'])

id_to_title = dict(zip(movies['movieId'], movies['title']))

def get_movies_seen_by_user(user_id):
    seen_movies = ratings[ratings['userId'] == user_id]['movieId']
    
    seen_movies_titles = [id_to_title[movie_id] for movie_id in seen_movies if movie_id in id_to_title]
    
    return seen_movies_titles

user_id = 4
movies_seen = get_movies_seen_by_user(user_id)

print(f"Películas vistas por el usuario {user_id}:")
for title in movies_seen:
    print(f"- {title}")
