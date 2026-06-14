### Finding the most frequent element

arr = [1, 2, 2, 3, 2, 1]

freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

sorted_arr = sorted(freq.items(), key = lambda x: -x[1])
print(sorted_arr[0][0], 'occured', sorted_arr[0][1], 'times')

print("Sorted array:", sorted_arr)