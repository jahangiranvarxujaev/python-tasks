x = int(input("? "))
y = int(input("? "))
x1 = int(input("? "))
y1 = int(input("? "))
a = abs(x - x1)
b = abs(y - y1)
if ((a == 1) and (b == 1)) or ((a == 0) and (b == 1)) or ((a == 1) & (b == 0)):
    print('может')
else:
    print('не может')
    
