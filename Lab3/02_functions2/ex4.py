"""
Write a function that takes a list of movies and computes the average IMDB score.
"""

def func(movies):
    sum = 0
    for i in movies:
        sum+=i['imdb']
    return round(sum/len(movies),2)


print(func(movies))