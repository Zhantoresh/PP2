"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy(nums_list): 
    for i in range(len(nums_list) - 1):
        if nums_list[i] == '0' and nums_list[i + 1] == '0' and nums_list[i+2]=='7': 
            return True
    return False

nums = input("Enter a list of numbers separated by space: ")
nums_list = nums.split()
print(spy(nums_list))
