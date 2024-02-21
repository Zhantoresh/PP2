'''
Define a function with a generator which can iterate the numbers, 
which are divisible by 3 and 4, between a given range 0 and n.
'''
def generate(n):
    for i in range(1,n+1):
        if i%3==0 and i%4==0:
            yield i
            
n = int(input("Enter:"))
generate_numbers = generate(n)
for num in generate_numbers:
    print(num)
