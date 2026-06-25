## --- INSERTION SORT ---

# 1. Start with the first element (sorted by default).
# 2. Pick the next element.
# 3. Compare it with elements in the sorted part.
# 4. Shift larger elements one step to the right.
# 5. Insert the picked element into the correct position.
# 6. Repeat until all elements are sorted.


arr = [1, 8, 9, 3, 2, 5, 5, 6]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key     

    return arr

print(insertion_sort(arr))   
