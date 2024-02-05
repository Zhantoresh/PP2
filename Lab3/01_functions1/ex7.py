"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

def has_33(nums_list):
    for i in range(len(nums_list) - 1):
        if nums_list[i] == '3' and nums_list[i + 1] == '3':
            return True
    return False

nums = input("Enter a list of numbers separated by space: ")
nums_list = nums.split()
print(has_33(nums_list))