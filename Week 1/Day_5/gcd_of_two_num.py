## GCD of two numbers
## Euclidean Algorithm:
# If one number is zero, GCD is the other number
# Else, gcd(a, b) = gcd(b, b%a)
# Continue until the remainder becomes zero. The non-zero number at that point is the GCD

def gcd(a: int, b: int):
    while b != 0:
        rem = a % b
        a, b = b, rem
    return a
print(gcd(18, 48))