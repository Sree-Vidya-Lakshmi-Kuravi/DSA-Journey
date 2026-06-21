### Basic Recursion

# Printing the sum of first N natural numbers

def sum_of_first_N(n: int):
    if n == 0:
        return 0
    return n + sum_of_first_N(n-1)  
    
print(sum_of_first_N(5))
    