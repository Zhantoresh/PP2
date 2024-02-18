#dates
import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
'''
print(today)
print(yesterday)
print(today-yesterday)
print(today.strftime("%A/%B/%D"))
'''



#
'''
print(max(2,-5,10))
print(min(-2,-5,8))

print(abs(-6))
print(pow(4,3))

import math

print(math.ceil(2.1))
print(math.floor(2.9))

print(math.sqrt(64))

print(math.pi)
'''

nums = [1,2,3,4,5]
for num in nums:
    print(num)
nums_iter = iter(nums)
print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))


for num in nums_iter:
    print(num)



class Mynums:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a+=1
        return x

mynums = Mynums()
miter = iter(mynums)


for num in mynums:
    print(num)

    

