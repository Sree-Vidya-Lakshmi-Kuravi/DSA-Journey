## Basic Hashing

# Count the occurrences of arraay elements

arr = [1, 2, 3, 4, 5, 2, 1, 3, 4, 6, 3, 2, 5]

def count_occurrences(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    print("The occurrences:")
    print(freq)

count_occurrences(arr) 