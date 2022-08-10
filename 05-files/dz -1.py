"""Информация о файле
Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:

количество букв латинского алфавита;
число слов;
число строк.
Пример ввода и вывода"""


counter_of_letters = 0
counter_of_words = 0
lines = 0
with open("alice.txt", encoding='utf-8') as alice_text:
    alice_txt = alice_text.read()
    alice_words = alice_txt.split()

    for word in alice_txt:
        for char in word:
            if str(char).isspace():
                continue
            counter_of_letters += len(char)

print(len(alice_words)+1, " words", counter_of_letters, 'letters')

file = open('alice.txt')
lines = 0
for line in file:
    lines += 1
print(lines, "Lines")
file.close()
