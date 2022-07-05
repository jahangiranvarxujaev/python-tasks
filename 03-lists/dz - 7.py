numbers = [1, 2, 3, 1, 2, 3]

for i in range(len(numbers)):
    for number in numbers:
        if number == numbers[i]:
            count = count +1
            if count > 2:
                 del number in numbers
