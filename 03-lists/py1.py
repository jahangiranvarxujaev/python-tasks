numbers = [1, 2, 3, 1, 2, 3]
i = 0

for i in range(len(numbers)):
    for number in numbers:
        if number == numbers[i]:
            count = count + 1


