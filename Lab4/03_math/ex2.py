'''
Write a Python program to calculate the area of a trapezoid.

Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
'''

first_value = int(input("Enter the first value:"))
second_value = int(input("Enter the second value:"))
height = int(input("Enter the value of height:"))
area = (first_value + second_value)*height*0.5
print("area is:", area)