#Удалить в массиве все числа, которые повторяются более двух раз.
numbers = list(map(int, input().split()))

list_1 = []
final_list = []
for number in numbers:
    list_1.append(number)
    if list_1.count(number) <= 1:
        final_list.append(number)
print(final_list)


