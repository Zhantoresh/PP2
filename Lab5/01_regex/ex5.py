'''
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
'''
import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()


def match_a_followed_by_b(content):
    pattern = re.compile(r'а.*б$')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("последовательность одной заглавной буквы, за которой следуют строчные буквы:")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

match_a_followed_by_b(content)