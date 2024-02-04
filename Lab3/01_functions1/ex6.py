"""
Write a function that accepts string from user, return a sentence with the words reversed. 
We are ready -> ready are We
"""

def text_reversed(text):
    words = text.split()
    i = len(words) - 1
    while i >= 0:
        print(words[i], end=' ')
        i -= 1

text = input('Enter text: ')
text_reversed(text)