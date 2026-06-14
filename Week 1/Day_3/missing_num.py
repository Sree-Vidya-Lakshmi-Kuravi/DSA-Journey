### Finding missing element

arr = [8, 2, 4, 5, 3, 7, 1]

actual_sum = sum(arr)
n = max(arr)
expected_sum = (n * (n + 1))//2

print(expected_sum - actual_sum)