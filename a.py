def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]


phrase = input("Enter a phrase: ")
if is_palindrome(phrase):
    print("The phrase is a palindrome.")
else:
    print("The phrase is not a palindrome.")



