### Counting all digits in a number
def count_dig(n: int):
    count = 0  # counting the digits
    while n > 0:
        n //= 10  # removes the last digit
        count += 1
    print(f"Number of digits in {n}:", count)

count_dig(23122004)
