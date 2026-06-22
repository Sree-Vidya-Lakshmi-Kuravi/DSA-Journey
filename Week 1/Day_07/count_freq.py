### Basic Hashing
# Counting frequency of array elements

arr = [1, 2, 3, 4, 2, 1, 4, 5, 6, 5, 3, 1, 2, 4, 6]

def count_freq(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    print("The occurrences:")
    return freq

print(count_freq(arr))