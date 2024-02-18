'''
Write a program using generator to print the even numbers between 
0 and n in comma separated form where n is input from console.
'''
def generate(n):
    for i in range(0, n + 1, 2):
        yield str(i)

n = int(input("Enter: "))
evensgenerator = generate(n)

print("Even numbers between 0 and", n, "in comma separated form:")
for idx, num in enumerate(evensgenerator):
    if idx == 0:
        print(num, end="")
    else:
        print(", " + num, end="")

