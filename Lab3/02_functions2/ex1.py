"""
Write a function that takes a single movie and returns True if its IMDB score is above 5.5
"""

def score_5_5(movie_name):
    for m in movies:
        if m['name'] == movie_name:
            if m['imdb'] > 5.5:
                return True
    return False

film = input("Enter the name of the movie:")
print(score_5_5(film))