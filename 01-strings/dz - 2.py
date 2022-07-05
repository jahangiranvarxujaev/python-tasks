'''
все слова из 5 символов
'''
a = input('Some words?? ')
words = a.split(' ')
for word in words:
    if len(word) == 5:
        print(word)
        
