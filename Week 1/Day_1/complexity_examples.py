### What is an Algorithm?
# An algorithm is the set of instructions that are given to solve a problem optimally by time and space. 

### What is Time Complexity?
# - Time complexity calculates how much the runtime of an algorithm increases as the input size grows.
# - It is independent of machine used and depends completely on number of basic operations

### What is Space Complexity?
# - Measures the total amount of memory space required by an algorithm to execute as a function of input size. 


 # Irrespective of array size, it returns only first element. It takes only one step.
def constant(arr):
    return arr[0]

# Returns every element in an array. Number of steps depends on the size of array
def linear(arr):
    for i in arr:
        print(i)

# Returns every element double time.
def quadratic(arr):
    for i in arr:
        for j in arr:
            print(i, j)