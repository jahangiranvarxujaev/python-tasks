'''
Сформировать строку из 10 символов. На четных позициях должны находится четные
цифры, на нечетных позициях - буквы.
'''
a = input("Word? ")
b = list(a)
b[1] = 1
b[3] = 3
b[5] = 5
b[7] = 7 
b[9] = 9
print(b)
