"""user = input()
with open("infinity.txt", encoding='utf-8') as infinity:
    infinity_read = infinity.read()
    infinity_list = infinity_read.split(' ')
    for x in infinity_list:
        if str(user) == str(x):
            print('in infinity')
"""
user = input()
file = open('infinity.txt')
file1 = file.read()
if user in file1:
    print('in file - infinity')
else:
    print('not in file - infinity')
file.close()
file = open('info.txt')
file2 = file.read()
if user in file2:
    print('in file - info')
else:
    print('not in file - info')