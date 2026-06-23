## --- BUBBLE SORT --

# 1. Start at the beginning of the list
# 2. Compare two neighboring elements
# 3. If left element is bigger, swap them
# 4. Keep going until the end, the largest element will be at end
# 5. Repeat the process for remaining unsorted part
# 6. Stop when no swaps are needed


arr = [8, 9, 3, 2, 5, 5, 6, 1]
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

print(bubble_sort(arr))
