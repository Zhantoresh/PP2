"""
You are given list of numbers separated by spaces. 
Write a function filter_prime which will take 
list of numbers as an agrument and returns only prime numbers from the list."""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

arr = (input("Enter the elements of list:"))
numbers = arr.split()
result = [x for x in numbers if is_prime(int(x)) ]
print("Prime numbers are:", result)


