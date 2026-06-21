### Basic Recursion

# Finding the fibonacci series

def fibo(n: int):
    if n <= 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    a = fibo(n-1)
    b = fibo(n-2)
    return a + b

print(fibo(3))

for i in range(1, 4):
    print(fibo(i), end = " ")