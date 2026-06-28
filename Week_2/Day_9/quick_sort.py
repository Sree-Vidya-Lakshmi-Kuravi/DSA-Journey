## Quick Sort

## Using pivot as the last element

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
# quickSort(arr, 0, len(arr) - 1)
# print(arr) 



### Using pivot as first element

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1  # position
    right = high   # position

    while True:
        # Move until the left element is lesser than pivot
        while left <= right and arr[left] < pivot:
            left += 1
        
        # Move until the right element is greater than pivot
        while left <= right and arr[right] > pivot:
            right -= 1

        if left > right:
            break

        # Swap the elements
        arr[left], arr[right] = arr[right], arr[left]

    # Place the pivot in the correct place
    arr[low], arr[right] = arr[right], arr[low]

    return right

def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1) 
        quickSort(arr, pivot_index + 1, high) 

arr = [4, 3, 2, 1]
quickSort(arr, 0, len(arr) - 1)
print(arr) 





