def spy(nums_list): 
    for i in range(len(nums_list) - 1):
        if nums_list[i] == '0' and nums_list[i + 1] == '0' and nums_list[i+2]=='7': 
            return True
    return False

nums = input("Enter a list of numbers separated by space: ")
nums_list = nums.split()
print(spy(nums_list))
