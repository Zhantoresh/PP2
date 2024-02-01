"""
Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
"""

def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if (2 * c) + (4 * r) == numlegs:
            return c, r
    return None


numheads, numlegs = map(int, input().split())
result = solve(numheads, numlegs)
if result is not None:
    chickens, rabbits = result
    print("Number of chickens:", chickens)
    print("Number of rabbits:", rabbits)
else:
    print("No solution for this case")