
#все слова n ного кол.

a = list(map(input().split()))
n = 5
for x in a:
    if len(x) == n:
        print(x)
    else:
        continue
