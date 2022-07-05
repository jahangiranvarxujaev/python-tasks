a = list(map(int, input().split()))
x = int(input())
b = a.count(x)
if b > 0:
    print("yes")
else:
    print("no")
