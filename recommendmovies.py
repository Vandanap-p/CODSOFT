import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
file_path = r"C:\Users\91701\Downloads\Movie-Dataset.csv"  
movies = pd.read_csv(file_path)
movies['genre'] = movies['genre'].str.replace('|', ' ')
count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split())
genre_matrix = count_vectorizer.fit_transform(movies['genre'])
similarity_matrix = cosine_similarity(genre_matrix)
def recommend_movies(movie_title, movies, similarity_matrix):
    try:
        movie_index = movies[movies['movie_name'] == movie_title].index[0]
        similarity_scores = list(enumerate(similarity_matrix[movie_index]))
        sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        recommended_movie_indices = [i[0] for i in sorted_movies[1:6]]
        return movies.iloc[recommended_movie_indices]['movie_name'].values
    except IndexError:
        return ["Movie not found in dataset! Please check the title spelling."]
user_favorite_movie = '3 Idiots'  
recommended_movies = recommend_movies(user_favorite_movie, movies, similarity_matrix)
print(f"Movies recommended for '{user_favorite_movie}':\n")
for movie in recommended_movies:
    print(movie)
