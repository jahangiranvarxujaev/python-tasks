numbers = list(map(int, input().split()))
common_list = []
final_list = []
for i in numbers:
    common_list.append(i)
    if common_list.count(i) <= 1:
        final_list.append(i)
print(final_list)