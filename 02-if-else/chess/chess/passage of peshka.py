x = int(input("? "))
y = int(input("? "))
x1 = int(input("? "))
y1 = int(input("? "))
a = x - x1
b = y - y1
if (a == -1) & (b == 1):
    print('атакует')
elif (x == x1) & (b == -1):
    print('может')
elif (y == 2) or (y == 7):
    if (x == x1) and (b == -2):
        print('может')
    else:
        pass
else:
    print('не может')
