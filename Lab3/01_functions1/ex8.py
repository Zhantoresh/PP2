"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy_game(num_list):
    sequence = [0, 0, 7]
    seq_index = 0
    for num in num_list:
        if num == sequence[seq_index]:
            seq_index += 1
            if seq_index == len(sequence):
                return True
    return False

nums = input("Enter numbers of list separated by spaces: ")
num_list = [int(elem) for elem in nums.split()] 
print(spy_game(num_list))