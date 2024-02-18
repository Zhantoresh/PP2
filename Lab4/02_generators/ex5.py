'''
Implement a generator that returns all numbers from (n) down to 0.
'''
def generate(n):
    for i in range(n,-1,-1):
        yield i
n = int(input("Enter:"))
fum = generate(n)
for num in fum:
    print(num)