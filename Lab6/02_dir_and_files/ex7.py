'''
Write a Python program to copy the contents of a file to another file
'''
with open("builtin_func.txt", "r") as f1:
    f2 = open(f"copy_builtin_func.txt", "w")
    for line in f1:
        f2.write(line)
    f1.close()