### Second largest element in an array

arr = [7, 45, 63, 69, 72, 46]

# set_arr = set(arr)
# sorted_arr = sorted(list(set_arr), reverse = True)

# print("Second largest element:", sorted_arr[1])


def second_largest(arr):
    set_arr = set(arr)
    sorted_arr = sorted(list(set_arr), reverse = True)

    if len(sorted_arr) == 1:
        return -1
    else:
        return sorted_arr[1]

print(second_largest(arr))