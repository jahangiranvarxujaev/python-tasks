"""# f = open('file.txt', 'w')
# f.write("first line \n")
# f.close()

initial_words = input()
list_words = initial_words.split(' ')
info_store = {}
final_text = ''
with open('alice.txt', encoding="utf-8") as alice_text:
    alice_read = alice_text.read()
    for x in list_words:
        info_store[x] = alice_read.count(x)

with open('info.txt', mode='w', encoding="utf-8") as info_text:
    for key, value in info_store.items():
        final_text = str(key) + '-' + str(value) + '\n'
        info_text.write(final_text)

with open('info.txt', encoding="utf-8") as info_text:
    print(info_text.read())
"""
store = {}
questions = ['What is Your name?', 'Who are you?']
answer = ''
final_store = ''

with open('infinity.txt', mode='w', encoding='utf-8') as infinity:
    while answer != str(0):
        for question in questions:
            print(question)
            answer = str(input("Your answer: "))
            if answer == str(0):
                break
            store[question] = answer
    for key, value in store.items():
        final_store = str(key) + " "*- + str(value) + '\n'
        infinity.write(final_store)



    # infinity.write()


