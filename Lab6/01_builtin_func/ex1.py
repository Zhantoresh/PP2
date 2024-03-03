'''
Write a Python program with builtin function to multiply all the numbers in a list
'''
import math
def multiply_numbers(numbers):
    return math.prod(numbers)

list1 = input("Enter the numbers separated by spaces: ")
numbers = [int(num) for num in list1.split()]
result = multiply_numbers(numbers)
print("Result:", result)