### Basic Recursion

# printing numbers 1 to N
def print_1_to_N(curr: int, n: int):
    if curr > n:
        return "Limit reached"
    print(curr)
    print_1_to_N(curr + 1, n)
print_1_to_N(1, 5)