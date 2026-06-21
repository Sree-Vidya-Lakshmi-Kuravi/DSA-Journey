## Basic Recursion

# Printing N to 1 using recursion
def print_N_to_1(n: int):
    if n < 1:
        return "Limit reached"
    print(n)
    print_N_to_1(n-1)
print(print_1_to_N(5))