'''
Write a Python program to list only directories, files and all directories, files in a specified path.
'''
import os
path = input("Enter a path: ")  # C:\user\user\dirnames\
# Перечислите все каталоги в пути
print("Directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

# Список всех файлов в пути
print("Files: ")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)

# Список всех каталогов и файлов в пути
print("Directories and Files: ")
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        print('Directory: ', os.path.join(dirpath, dirname))
    for filename in filenames:
        print('File:', os.path.join(dirpath, filename))