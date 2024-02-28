'''
Write a Python program to replace all occurrences of space, comma, or dot with a colon.
'''

import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()


def replace_with_colon(content):
    result_string = content.replace(' ', ':').replace(',', ':').replace('.', ':')
    return result_string


text = 'Hello, world. This is a test.'
print(replace_with_colon(text))