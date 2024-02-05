"""
Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set.
"""


def unique(num_list):
    arr = []
    for i in num_list:
        if i not in arr:
            arr.append(i)
    return arr

nums = input("Enter the nums:")
num_list = nums.split()
res = unique(num_list)
print(res)