"""
Write a function that computes the volume of a sphere given its radius.
"""
import math
def volume_of_sphere(radius):
    return (4/3) * math.pi * radius**3

r = float(input("Enter a value of radius: "))
print("volume of a sphere with radius", r ,"is:",volume_of_sphere(r))