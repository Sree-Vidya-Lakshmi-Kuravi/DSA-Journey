## Recursive Bubble sort

def bubble_sort(arr):
    if len(arr) == 1:
        return arr

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [2,6,1,3,7,4]
# print(bubble_sort(arr))



n = len(arr)
def rec_bubble_sort(arr, n):
    if n == 1:
        return arr

    for j in range(n - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

    rec_bubble_sort(arr, n - 1)

arr = [2,2,1,3,6,4]
print("Before:", arr)

print("After:")
rec_bubble_sort(arr, n)
print(arr)
