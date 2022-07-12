string = input()
initial_list = string.split(' ')
print(initial_list)
common_list = []
final_list = []

for word in initial_list:
    common_list.append(word)
    if common_list.count(word)