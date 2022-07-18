"""Информация о файле
Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:

количество букв латинского алфавита;
число слов;
число строк.
Пример ввода и вывода
"""
counterofletters = 0
with open("alice.txt", encoding='utf-8') as alice_text:
    alice_read = alice_text.read()
    counterofwords = 0
    list1 = alice_read.split(" ")
    for word in alice_read:
        for count in word:
            if str(count).isspace():
                continue
            counterofletters = counterofletters +  len(count)
    for x in list1:
        counterofwords = counterofwords + 1
print(counterofwords, " words", counterofletters, 'letters')
