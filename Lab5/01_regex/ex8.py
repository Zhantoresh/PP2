'''
Write a Python program to split a string at uppercase letters.
'''
import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()


def split_at_uppercase(input_string):
    result = re.findall('[A-Z][^A-Z]*', input_string)
    return result