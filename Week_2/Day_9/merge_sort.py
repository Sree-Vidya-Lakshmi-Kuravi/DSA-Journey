### Merge sort

arr = [38, 27, 43, 3]

# splitting (dividing)
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2  # divides even len(arr) is odd
    left = mergeSort(arr[:mid])  # from start to mid
    right= mergeSort(arr[mid:])  # from mid to end

    return merge(left, right)

# merging (joining)
def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res

print(mergeSort(arr))
             
