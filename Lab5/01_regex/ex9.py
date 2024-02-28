'''
Write a Python program to insert spaces between words starting with capital letters.
'''

import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()

def capital_letters(input_string):
    res = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return res


cnt = "SplitThisStringAtUppercaseLetters"

print(f"Resulting list: {split_at_uppercase(cnt)}\nResult string: {capital_letters(cnt)}")