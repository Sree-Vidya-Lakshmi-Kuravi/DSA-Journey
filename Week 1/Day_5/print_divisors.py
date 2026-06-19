### Print all divisors

def all_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    print(f"Divisors of {n}:", divisors)
all_divisors(78)