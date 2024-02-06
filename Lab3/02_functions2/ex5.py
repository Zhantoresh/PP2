"""
Write a function that takes a category and computes the average IMDB score.
"""

def category_computes_average(category):
    sum_category_movie = 0
    result = []
    for m in movies:
        if m['category'] == category:
            result.append(m['name'])
            sum_category_movie += m['imdb']
    return sum_category_movie/len(result)
    
category = input("Enter the name of the category:")
print(category_computes_average(category))