'''
изменить первое слово на посленднюю
'''
a = input("Some words?? ")
b = a.split(' ')
print(b)
c = a[0]
b[0] = b[-1]
b[-1] = c
print(b)
