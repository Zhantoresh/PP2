"""
Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""

import random

def find_num_random(rand_num, count):
    count += 1
    num = int(input('Take a guess.\n'))
    if num == rand_num:
        print('Good job, KBTU! You guessed my number in', count, 'guesses!')
        return
    print('\nYour guess is too low.')
    return find_num_random(rand_num, count)

name = input('Hello! What is your name?\n')
number = random.randint(1, 20)
count = 0
print('Well,', name, ', I am thinking of a number between 1 and 20.\n')
find_num_random(number, count)