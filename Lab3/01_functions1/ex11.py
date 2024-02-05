"""
Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same 
backward as forward, e.g., madam
"""

def reversed_str(w_list):
    result = ''
    i = len(w_list) - 1
    while i >= 0:
        result += w_list[i]
        i -= 1
    return result

def palindrome(word):
    reversed_word = reversed_str([char for char in word])
    return word == reversed_word

word = input("Enter a word: ")
is_palindrome = palindrome(word)
print(word + " is a palindrome: " + str(is_palindrome))