# ### Counting occurrences of a target

# arr = [1, 2, 2, 3, 2]
# target = 2

# freq = {}

# for i in arr:
#     if i == target:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1

# for i, j in freq.items():
#     print("Number of times target occurred:", j)



def count_occur(arr, target):
    t_count = 0
    for i in arr:
        if i == target:
            t_count += 1

    print("Target Count:", t_count) 

arr = [1, 2, 2, 3, 2]
target = 2

count_occur(arr, target)