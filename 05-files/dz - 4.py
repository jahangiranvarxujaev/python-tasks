file = open('ban')
ban_words = file.read().split(' ')
print(ban_words)
file.close()
file = open('ban-text')
file_list = file.read().split(' ')
i = 0
for x in ban_words:
    i = 0
    while i < len(file_list):
        if x == file_list[i]:
            a = len(file_list[i])
            b = a * '*'
            file_list.insert(i, b)
            file_list.remove(file_list[i+1])
        i += 1

print(file_list)