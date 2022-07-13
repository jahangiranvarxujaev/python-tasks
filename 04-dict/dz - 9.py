string = input()
initial_list = string.split(' ')
print(initial_list)
common_list = {}
final_list = []

for word in initial_list:
    common_list[word] = common_list.get(word, 0) + 1

min_value = 99999999
final_key = ''
for key, value in common_list.items():
    if value < min_value:
        min_value = value
        final_key = key

    # else:
    #     final_key =

print(final_key)