### Armstrong number

def armstrong(n):
    num_list = list(str(n))
    l = len(num_list)
    sum = 0

    for ele in num_list:
        ele = int(ele) ** l
        sum += ele
    if sum == n:
        print("Armstrong")
    else:
        print("Not an armstrong number")

# armstrong(153)

n = 1634
dup = n
armstrong_num = 0
c = 0
while dup != 0:
    c += 1
    dup //= 10

dup1 = n
while dup1 != 0:
    dig = dup1 % 10
    armstrong_num += dig ** c
    dup1 //= 10

if n == armstrong_num:
    print(f"{n} is an armstrog number")
else:
    print(f"{n} is not an armstrog number")