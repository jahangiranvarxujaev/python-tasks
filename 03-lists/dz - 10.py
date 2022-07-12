#четные,нечетные,фибоначчи  числа через массивы
list1 = [0, 1]
i = 0
b = 0
while i < 101:
    b = list1[i] + list1[i+1]
    list1.append(b)
    i += 1
print(list1)

for number in list1:
    if number % 2 == 0:
        print(number)
    else:
        continue