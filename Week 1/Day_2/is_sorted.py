### Check whether the array is sorted or not

arr = [7, 45, 63, 69, 72, 46]
sorted_arr = sorted(arr, reverse = False)

def check_arr_sorted(arr, sorted_arr):
    if arr == sorted_arr:
        return True
    return False

# print(check_arr_sorted(arr, sorted_arr))


### Alternate solution
arr = [7, 45, 63, 69, 72, 46]
is_sorted = True

for i in range(1, len(arr) - 1):
    if arr[0] > arr[i]:
        is_sorted = False
        break
    elif arr[0] <= arr[i]:
        arr[0] = arr[i]

print(is_sorted)