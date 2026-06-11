### Reversing the array

arr = [7, 45, 63, 69, 72, 46]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array:", arr)