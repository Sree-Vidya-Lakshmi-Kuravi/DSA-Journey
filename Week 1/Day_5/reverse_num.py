### Reversing a number
def rev_num(n: int):
    # n = list(str(n))
    # l = 0
    # r = len(n)-1
    # while l < r:
    #     n[l], n[r] = n[r], n[l]
    #     l += 1
    #     r -= 1
    # n = "".join(n)
    # print("Reversed Number:", n)

    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    print("Reversed Number:", rev)

# rev_num(2312)


## Palindrome
def palindrome(n):
    revNum = 0
    while n > 0:
        unit = n % 10  # last digit 
        revNum = revNum * 10 + unit
        n //= 10
    if n == revNum:
        return True
    else:
        return False
# print(palindrome(2312132))