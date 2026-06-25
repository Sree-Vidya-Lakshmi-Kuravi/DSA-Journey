## Recursive Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # value
        # print("Key:", key)
        j = i-1  # left element position of i i.e., 0

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

arr = [8, 4, 2, 5, 9]
# print(insertion_sort(arr))


def rec_ins_sort(arr, n, pos):
    if pos == n:
        return arr

    key = arr[pos]
    j = pos - 1

    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    
    arr[j+1] = key
    return rec_ins_sort(arr, n, pos+1)

arr = [8, 4, 2, 5, 9]
print("Before:", arr)

print("After:")
rec_ins_sort(arr, len(arr), 1)
print(arr)


