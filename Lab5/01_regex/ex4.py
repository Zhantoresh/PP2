'''
Write a Python program to find the sequences of one upper case letter followed by lower case letters.
'''
import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()


def find_upper_case_letter_followed_by_lower(content):
    pattern = re.compile(r'\b[A-Z]{1}[a-z]+\b') # r'\b[А-Я]{1}+[а-я]+\b'
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("последовательность одной заглавной буквы, за которой следуют строчные буквы:")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

find_upper_case_letter_followed_by_lower(content)