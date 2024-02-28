'''
Write a Python program to convert a given camel case string to snake case.
'''
import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()

def camel_to_snake(camel_case):
    res = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case)
    return res.lower()

camel = "helloWorldExample"
snake_case = camel_to_snake(camel)

print(f"Camel case: {snake_case}")