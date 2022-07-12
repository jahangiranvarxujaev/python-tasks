#Определить, содержит ли массив данное число x
a = [12, 343, 76, 12, 778, 44, 780]
x = int(input())
b = a.count(x)
if b > 0:
    print("yes")
else:
    print("no")
