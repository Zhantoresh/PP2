'''
Write a python program to convert snake case string to camel case string.
'''

import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()


def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case)

snake = "hello_world_example"
camel_case = snake_to_camel(snake)

print(f"Camel case: {camel_case}")