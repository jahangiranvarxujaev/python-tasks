numbers = [1, 2, 3, 1, 2, 3]

for i in range(len(numbers)):
    for number in numbers:
        if number == numbers[i]:
            del number in numbers
print(numbers)