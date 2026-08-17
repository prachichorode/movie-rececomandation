# CODSOFT Task 4: Movie Recommendation System

movies = {
    "Inception": "Action Sci-Fi Thriller",
    "Interstellar": "Adventure Sci-Fi Drama",
    "The Matrix": "Action Sci-Fi Thriller",
    "Avengers": "Action Adventure Superhero",
    "Iron Man": "Action Adventure Superhero",
    "Titanic": "Romance Drama",
    "The Notebook": "Romance Drama",
    "Jurassic Park": "Adventure Sci-Fi Thriller",
    "Avatar": "Action Adventure Sci-Fi"
}


def recommend_movies(selected_movie):

    selected_genres = set(
        movies[selected_movie].lower().split()
    )

    scores = {}

    for movie, genres in movies.items():

        if movie == selected_movie:
            continue

        movie_genres = set(
            genres.lower().split()
        )

        common_genres = selected_genres.intersection(movie_genres)

        scores[movie] = len(common_genres)

    recommendations = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations[:5]


print("===== MOVIE RECOMMENDATION SYSTEM =====")

print("\nAvailable Movies:")

for movie in movies:
    print("-", movie)


# Take movie name from user
selected_movie = input("\nEnter a movie name: ").strip().title()


if selected_movie in movies:

    recommendations = recommend_movies(selected_movie)

    print("\nRecommended Movies:")

    for movie, score in recommendations:
        print(movie, "- Similarity Score:", score)

else:
    print("Movie not found.")