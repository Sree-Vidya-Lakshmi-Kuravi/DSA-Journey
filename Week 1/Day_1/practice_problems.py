arr = [4, 6, 2, 0, 8, 9]

# Find the largest element in an array.
print("Largest element:", max(arr))

# Find the sum of all elements in an array.
print("Sum:", sum(arr))

# Count the number of even elements in an array
even = []
odd = []
for a in arr:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)
    
print("Number of even elements:", len(even))