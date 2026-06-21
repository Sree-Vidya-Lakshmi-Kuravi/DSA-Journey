## Basic Recursion

# Print name N times using recursion
def print_name(n: int):
    if n == 0:
        return 0
    name = input("Enter the name:")
    print(name * n) 
    print_name(n-1)
print_name(4)
