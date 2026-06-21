## Basic Recursion

# Reversing the elements of an array

def rev_Array(arr: list):

    if len(arr) == 0:
        return 0

    l = 0
    r = len(arr) - 1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return arr
    print(rev_Array(arr))

# print(rev_Array([1, 2, 3, 4, 5, 7, 67, 90, 32]))


def rev_arr(arr: list, l, r):
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
    if l >= r:
        return arr
    return rev_arr(arr, l, r)

arr = [3,4,5,6]
print(rev_arr(arr, 0, len(arr) - 1))