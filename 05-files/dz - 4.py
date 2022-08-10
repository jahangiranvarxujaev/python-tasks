ban_words = input("words")

with open('ban', encoding='utf-8', mode='w') as file:
    file.write(ban_words)
    ban_words = ban_words.split(' ')

ban_text = input('text')
with open('ban-text', encoding='utf-8', mode='w') as file:
    file.write(ban_text)
    file_list = ban_text.split(' ')


for ban_word in ban_words:
    index = 0
    while index < len(file_list):
        if ban_word == file_list[index]:
            len_of_word = len(file_list[index])
            stars = len_of_word * '*'

            file_list.insert(index, stars)
            file_list.remove(file_list[index+1])
        elif ban_word in file_list[index]:
            for x in ban_word:
                for y in file_list[index]:
                    if x == y:
                        file_list.insert(index,'*')
                        file_list.remove(file_list[index])
        index += 1

print(file_list)
