"""
Write a function that accepts string from user and print all permutations of that string.
"""

from itertools import permutations

def print_permutations(input_string):
    permuted_strings = permutations(input_string)
    for permuted_string in permuted_strings:
        print(''.join(permuted_string))


input_string = input("Enter the string: ")
print_permutations(input_string)