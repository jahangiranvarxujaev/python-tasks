a = list(map(int, input().split()))
i = 0
b = 0
while i == len(a):
    if a[i] > a[i + 1]:
        b = b + 1
        i += 1
    else:
        continue

if len(a) - 1 == b:
    print("возрастающии")
else:
    print("убавающии")
