'''
Create a generator that generates the squares of numbers up to some number N.
'''
def generate_squares(n):
    for i in range(1, n+1):
        yield i**2

n = int(input("Enter: "))
squares_generator = generate_squares(n)

for square in squares_generator:
    print(square)