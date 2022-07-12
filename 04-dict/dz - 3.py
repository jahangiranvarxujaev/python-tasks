#3
list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict1 = {}
for key in list1:
    for value in list2:
        if int(key) == value:
            dict1[key] = list2[value - 1] ** 3
        else:
            continue

print(dict1)
