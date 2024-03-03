'''
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
'''
import time
import math

def calculate_square_root(number):
    return math.sqrt(number)

input_number = int(input("Enter the number: "))
delay_ms = int(input("Enter the delay time in milliseconds: "))

time.sleep(delay_ms / 1000)  
result = calculate_square_root(input_number)

print(f"The square root of number {input_number} after {delay_ms} milliseconds is {result}")