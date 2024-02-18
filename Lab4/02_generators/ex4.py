'''
Implement a generator called squares to yield the square of all numbers 
from (a) to (b). Test it with a "for" loop and print each of the yielded values.
'''

def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a,b = map(int,input().split())
fum = squares(a,b)
print("All squares of numbers from", a , "to",  b, ":")
for num in fum:
    print(num)