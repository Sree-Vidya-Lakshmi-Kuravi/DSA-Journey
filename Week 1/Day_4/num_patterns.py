### Number patterns

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def increase_num(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end = " ")
        print()
# increase_num(5)

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def num_repeat(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end = " ")
        print()
# num_repeat(5)

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def decrese_num(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end = " ")
        print()
# decrese_num(5)

# 1 
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

def zero_one(n):
    for i in range(n):
        if i%2 == 0:
            s = 1
        else:
            s = 0
    
        for j in range(i+1):
            print(s, end = " ")
            if s==0:
                s = 1
            else:
                s = 0
        print()
# zero_one(5)

# 1
# 2 3
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

def increase_num(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(num, end = " ")
            num += 1
        print()
# increase_num(5)

## Half butterfly using numbers
def half_butterfly(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end = " ")
        for j in range((n-i)*2, 0, -1):
            print(" ", end = " ")
        for j in range(i, 0, -1):
            print(j, end = " ")
        print()
# half_butterfly(4)


# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4 

def square_num(n):
    size = 2 * n - 1
    for i in range(size): 
        for j in range(size):
            top = i  # row
            left = j # column
            bottom = size - 1 - i
            right = size - 1 - j

            layer = min(top, bottom, left, right)
            value = n - layer

            print(value, end = " ")
        print()
# square_num(4)