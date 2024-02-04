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

def filter_prime(num_list):
    prime_list = [num for num in num_list if is_prime(num)]
    return prime_list

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)

