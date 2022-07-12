#Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго —
# соответственно значениями нашего словаря.
list1 = ['name', 'age', 'school']
list2 = ['jahongir', 14, 'DIS']
dict1 = {}
value = -1
for key in list1:
    for value in range(len(list2)):
        dict1[key] = list2[value]
print(dict1)
