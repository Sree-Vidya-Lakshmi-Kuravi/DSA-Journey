## Star Patterns

# *****
# *****
# *****
# *****
# *****

def square(n):
    for i in range(0, n):
        for j in range(0, n):
            print("*", end = " ")
        print()
# square(5)


## Right - angle triangle
# *
# **
# ***
# ****
# *****

def right_angle_tri(n):
    for i in range(0, n + 1):
        for j in range(i):
            print("*", end = " ")
        print()
# right_angle_tri(5)


## Reverse right angle triangle
# *****
# ****
# ***
# **
# * 

def rev_right_angle_tri(n):
    for i in range(n+1):
        for j in range(i, n):
            print("*", end = " ")
        print()
# rev_right_angle_tri(5)


## Equilateral triangle
#     *
#    ***
#   *****
#  *******
# *********

def equi_tri(n):
    for i in range(0, n):
        for s in range(0, (n-i)+1):
            print(" ", end = " ")
        for j in range(i*2 + 1):
            print('*', end = " ")
        print()
# equi_tri(n)


## Reverse Equilateral triangle
# *********
#  *******
#   *****
#    ***
#     *

def rev_equi_tri(n):
    for i in range(0, n):
        for s in range(0, i):
            print(" ", end = " ")
        for j in range(((n-i)*2)-1, 0, -1):
            print("*", end = " ")
        print()
# rev_equi_tri(5)

#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def diamond(n):
    # upward triangle
    for i in range(0, n):
        for s in range(0, (n-i)+1):
            print(" ", end = " ")
        for j in range(i*2 + 1):
            print('*', end = " ")
        print()

    # downward triangle
    for i in range(0, n):
        for s in range(0, i+2):
            print(" ", end = " ")
        for j in range(((n-i)*2)-1, 0, -1):
            print("*", end = " ")
        print()
# diamond(5)


## Arrow
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# * 

def arrow(n):
    # upward triangle
    for i in range(0, n+1):
        for j in range(i):
            print("*", end = " ")
        print()
    
    # downward triangle
    for i in range(n, 0, -1):
        for j in range(i-1):
            print("*", end = " ")
        print()
# arrow(5)


## Hollow diamond
def hollow_diamond(n):
    # upward triangle
    for i in range(n):
        for j in range(n-i):
            print("*", end = " ")
        for s in range((i*2) - 1):
            print(' ', end = " ")
        for k in range(n-i):
            print("*", end = " ")
        print()

    # downward triangle
    for i in range(n):
        for j in range(i+1):
            print("*", end = " ")
        for sp in range(((n-i-1)*2)-1, 0, -1):
            print(" ", end = " ")
        for j in range(i+1):
            print("*", end = " ")
        print()
# hollow_diamond(5)

def butterfly(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end='')
        for j in range((n - i) * 2 - 1):
            print(' ', end = '')
        for j in range(i + 1):
            print('*', end = '')
        print()
    for i in range(n):
        for j in range(n - i - 1):
            print('*', end = '')
        for j in range((i*2)+3):
            print(' ', end = '')
        for j in range(n - i - 1):
            print('*', end = '')
        print()
butterfly(5)