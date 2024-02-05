"""
Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******

"""

def histogram(n_list):
    for num in n_list:
        print(num * '*')

nums = input("Enter the nums separated by space: ")
n_list = [int(elem) for elem in nums.split()]
histogram(n_list)