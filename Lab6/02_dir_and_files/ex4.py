'''
Write a Python program to count the number of lines in a text file.
'''
f = open("text4.txt", "r")
print(len(f.readlines()))
f.close()