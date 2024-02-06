"""
Write a function that returns a sublist of movies with an IMDB score above 5.5.
"""

def score_5_5():
    result = []
    for m in movies:
        if m['imdb'] > 5.5:
                result.append(m['name'])
    return result

print(score_5_5())