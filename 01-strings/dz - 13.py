'''
 Дана строка. Вывести первые три символа и последний три символа, если длина строки больше 5. Иначе вывести первый символ столько раз, какова длина строки.
'''
a = input("Word? ")
b = len(a)
if a > 5:
  print(a[:3], a[-1:- 4])
else:
  print(a * b)
