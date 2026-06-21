## Basic Recursion
### Printing something N times

def print_N_times(n: int):
    if n == 0:
        return 0
    print(n)
    print_N_times(n-1)
# print_N_times(5)