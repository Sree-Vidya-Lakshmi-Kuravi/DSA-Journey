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
    
print(rev_Array([1, 2, 3, 4, 5, 7, 67, 90, 32]))