## GCD of two numbers
## Euclidean Algorithm:
# If one number is zero, GCD is the other number
# Else, gcd(a, b) = gcd(b, b%a)
# Continue until the remainder becomes zero. The non-zero number at that point is the GCD

def gcd_of_two_num(a: int, b: int):
    while b != 0:
        a, b = b, b%a
    return a
print(gcd_of_two_num(48, 18))