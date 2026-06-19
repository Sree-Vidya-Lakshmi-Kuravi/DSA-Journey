## Check whether a number is prime or not

def check_prime(n):
    if n == 2:
        print("Prime")
        return 
    elif n % 2 == 0:
        print("Not a prime")
        return 
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            print("Not a prime")
            return 
    print("Prime")

check_prime(12)