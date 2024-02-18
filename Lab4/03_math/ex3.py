'''
Write a Python program to calculate the area of regular polygon.

Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
'''
import math 

numofsides = int(input("Enter the number of sides:"))
length = int(input("Enter the value of the length of side:"))
area = (numofsides * length**2) / (4 * math.tan(math.pi / numofsides))
print("Area is:", round(area,2))