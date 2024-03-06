'''
Write a Python program with builtin function to multiply all the numbers in a list
'''
l = [1,2,3,4,5]
print("result:", eval('*'.join(str(item) for item in l))) 
