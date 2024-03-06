'''
Write a Python program to write a list to a file.
'''
f = open("text5.txt", "w")
li = input("Input a list of values separated by commas: ").split(", ")
f.write(str(li))
f.close()