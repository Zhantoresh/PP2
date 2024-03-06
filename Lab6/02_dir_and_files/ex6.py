'''
Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
'''
import os
from string import ascii_uppercase

new_path = "kbtu_pp2\\Lab6_pp2\\alphabet"
if not os.access(new_path, os.F_OK):
    os.makedirs(new_path)

for letter in ascii_uppercase:
    f = open(f"{new_path}\\{letter}.txt", "w")
    f.write(f"This is {letter}'s txt file")
    f.close()