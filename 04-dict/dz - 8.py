first_dict = {'1': 12, '2' : 23, '3' : 34}
second_dict = {'1': 67, '2' : 90, '3' : 34}
final = {}
for key1, value1 in first_dict.items():
    for key2, value2 in second_dict.items():
        if int(key1) == int(key2):
            final[key1] = value1 + value2

print(final)

