#найти количество чисел в массиве, которые делятся на 3, но не делятся на 7
a = list(map(int, input().split()))
b = 0
for x in a:
    if (x / 3) and (x % 7 != 0):
        b = b + 1
    else:
        continue
print(b)
