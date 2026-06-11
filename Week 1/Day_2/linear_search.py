### Linear Search

arr = [7, 45, 63, 69, 72, 46]
target = 69
pos = None

for i in range(len(arr)):
    if arr[i] == target:
        pos = i
        break

print(f"Element {target} found at {pos}")