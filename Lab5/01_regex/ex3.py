'''
Write a Python program to find sequences of lowercase letters joined with a underscore.
'''

import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()

def find_lowercase_sequences_with_underscore(content):
    pattern = re.compile(r'\b[a-z]+_[a-z]+\b')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("строки где :")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

find_lowercase_sequences_with_underscore(content)