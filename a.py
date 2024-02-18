movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]
'''
# Создаем словарь для подсчета количества фильмов по жанру
genre_count = {}

# Проходим по каждому фильму в списке и увеличиваем счетчик для каждого жанра
for movie in movies:
    category = movie["category"]
    if category in genre_count:
        genre_count[category] += 1
    else:
        genre_count[category] = 1

# Выводим результат
for genre, count in genre_count.items():
    print(f"Жанр: {genre}, количество фильмов: {count}")
'''

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def func():
    a = []
    for m in movies:
        if m['category'] == 'Thriller':
                a.append(m['name'])
    return a
print(func())
def func1():
    b = []
    for m in movies:
        if m['category'] == 'Action':
                b.append(m['name'])
    return b
print(func1())
def func2():
    c = []
    for m in movies:
        if m['category'] == 'Adventure':
                c.append(m['name'])
    return c
print(func2())
def func3():
    d = []
    for m in movies:
        if m['category'] == 'Romance':
                d.append(m['name'])
    return d
print(func3())
def func4():
    e = []
    for m in movies:
        if m['category'] == 'Suspense':
                e.append(m['name'])
    return e
print(func4())
def func5():
    f = []
    for m in movies:
        if m['category'] == 'Comedy':
                f.append(m['name'])
    return f
print(func5())
def func6():
    g = []
    for m in movies:
        if m['category'] == 'Crime':
                g.append(m['name'])
    return g
print(func6())
def func7():
    h = []
    for m in movies:
        if m['category'] == 'War':
                h.append(m['name'])
    return h
print(func7())
def func1():
    i = []
    for m in movies:
        if m['category'] == 'Drama':
                i.append(m['name'])
    return i
print(func7())



#Thriller action adventure romance suspense comedy crime war drama





