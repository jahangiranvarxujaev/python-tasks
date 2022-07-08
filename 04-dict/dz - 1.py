'''
#1
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

# 2
dictionary_1 = {'a': 300, 'b': 400, 'c': 500, 'd': 600}
b = 1
for i in dictionary_1.values():
    b = b * i
print(b)

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


#4
list1 = ['name', 'age', 'school']
list2 = ['jahongir', 14, 'DIS']
dict1 = {}
value = -1
for key in list1:
    for value in range(len(list2)):
        dict1[key] = list2[value]
print(dict1)

#5
a = 'pythonist'
dict1 = {}
for i in a:
    dict1[i] = a.count(i)
print(dict1)
'''
#6
