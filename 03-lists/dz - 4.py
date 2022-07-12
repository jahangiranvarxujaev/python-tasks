#четные,нечетные,фибоначчи  числа через массивы
numbers = [1, 2, 3, 1, 2, 3]
i = 0
count = 0
for i in range(len(numbers)):
    for number in numbers:
        if number == numbers[i]:
            count = count + 1

if count >= 2:
    print("yes")
else:
    print("no")
