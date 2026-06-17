### Alphabet patterns

# A
# A B
# A B C
# A B C D
# A B C D E
def chr_tri(n):
    for i in range(0, n+1):
        for j in range(0, i):
            print(chr(65 + j), end = " ")  
        print()
# chr_tri(5)


# A B C D E
# A B C D
# A B C
# A B
# A
def rev_chr_tri(n):
    for i in range(0, n+1):
        for j in range(0, n - i):
            print(chr(65 + j), end = " ")
        print()
# rev_chr_tri(5)


# A
# B B
# C C C
# D D D D
# E E E E E
def same_chr_tri(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print(chr(65 + i), end = " ")
        print()
# same_chr_tri(5)


#       A
#     A B A
#   A B C B A
# A B C D C B A

def pascal_tri(n):
    for i in range(0, n+1):
        for sp in range(0, (n-i)):
            print(" ", end = " ")

        p = (i*2 + 1)//2
        ch = ord('A')

        for j in range(0, i*2+1):
            print(chr(ch), end = " ")

            if j < p:
                ch += 1
            else:
                ch -= 1
        print()
pascal_tri(4)


# E            
# D E
# C D E
# B C D E
# A B C D E
def rev_tri_ch(n):
    for i in range(0, n):
        for j in range(0, (i+1)):
            print(chr(69 - i + j), end = " ")
        print()
# rev_tri_ch(5)