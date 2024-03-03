'''
Write a Python program with builtin function that checks whether a passed string is palindrome or not.
'''
stroka = str(input("Enter the string:"))
reversed_stroka = ''.join(reversed(stroka))
if reversed_stroka == stroka:
    print("String is a palindrome")
else:
    print("String isn't palindrome")