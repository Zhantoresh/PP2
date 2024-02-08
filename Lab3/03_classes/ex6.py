"""
Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions.
"""
class Prime_san:
    def __init__(self, nums):
        self.nums = nums

    def prime_ssan(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_fil(self):
        return list(filter(lambda x: self.prime_ssan(x), self.nums))

nums = list(map(int, input().split()))

prime_filter = Prime_san(nums)

prime_numbers = prime_filter.prime_fil()
print(prime_numbers)