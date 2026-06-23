### --- SELECTION SORT ---

# 1. Start with the first element
# 2. Find smallest element in the unsorted array
# 3. Swap it with the first unsorted element
# 4. Move boundary of sorted part one step forward
# 5. Repeat until all elements are sorted


arr = [7, 4, 3, 5, 1]
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            
        arr[j], arr[min_index] = arr[j], arr[min_index]
    
    return arr

print(selection_sort(arr))

