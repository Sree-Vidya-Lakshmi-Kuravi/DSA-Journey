## Basic Hashing
# Highest occurring element in array

arr = [1, 2, 3, 4, 5, 2, 1, 3, 4, 6, 3, 2, 5]

def highest_occurring(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    print("The occurrences:")
    print(freq)

    maximum = max(freq, key = freq.get)

    print("Highest occurring element:")
    print("Number:", maximum, "||", "Count:", freq[maximum])

highest_occurring(arr)    
