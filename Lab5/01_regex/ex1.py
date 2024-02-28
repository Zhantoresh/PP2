'''
Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
'''
import re

file_path = r'c:\Users\1\Desktop\PP2\Lab5\01_regex\row.txt'

with open('row.txt') as file:
    lines=file.readlines()

def find_a_followed_by_bs(content):
    pattern = re.compile(r'a+b*')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("строки где после a содержится ноль или несколько b:")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

find_a_followed_by_bs(content)