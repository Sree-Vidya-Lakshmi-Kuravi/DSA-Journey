## Quick Sort

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # initially, no element is smaller

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quickSort(arr, low, pivot_index - 1) # left sub array
        quickSort(arr, pivot_index + 1, high) # right sub array


arr = [4, 3, 2, 1]
quickSort(arr, 0, len(arr) - 1)
print(arr) 