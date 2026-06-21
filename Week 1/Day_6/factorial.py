## Basic Recursion

# Printing the factorial of given number

def fact(n: int):
    if n == 0:
        return 1

    return n * fact(n-1)

print(fact(6))