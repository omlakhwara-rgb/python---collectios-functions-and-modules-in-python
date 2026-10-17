"""
Q- 4.Given three lists — movie titles, genres, and ratings — use zip() to create a list of dictionaries where each dictionary contains keys 'title', 'genre', and 'rating' for a movie, then print the list.<br><br><em><strong>Constraint:</strong> Do not use any external libraries.</em>z
"""

titles = ["Inception", "KGF", "Dangal"]
genres = ["Sci-Fi", "Action", "Drama"]
ratings = [8.8, 8.2, 8.4]

movies = []

for t, g, r in zip(titles, genres, ratings):
    movies.append({"title": t, "genre": g, "rating": r})

print(movies)
