'''
Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
'''
import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()

def find_a_followed_by_2_to_3_bs(content):
    pattern = re.compile(r'a{1}b{2,3}')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("строки где после a содержатся два или три b:")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

find_a_followed_by_2_to_3_bs(content)