'''
Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
'''
import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()


def find_a_followed_by_bs(content):
    pattern = re.compile(r'а+б*')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("строки где содержиться после а ноль или несколько б:")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

find_a_followed_by_bs(content)