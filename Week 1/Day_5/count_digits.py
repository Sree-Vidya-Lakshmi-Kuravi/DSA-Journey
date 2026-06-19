### Counting all digits in a number
def count_dig(n: int):
    count = 0
    for i in str(n):
        d = n % 10
        count += 1
    print(f"Number of digits in {n}:", count)

# count_dig(23122004)