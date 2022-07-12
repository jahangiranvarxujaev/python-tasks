#В массиве заменить все числа, большие данного числа, на x

a = list(map(int, input().split()))
b = int(input())
x = 5
i = 0
c = len(a)
d = c - 1
for y in a:
    while i == d:
        if y - x == b:
            a[i] = 12
        else:
            continue
