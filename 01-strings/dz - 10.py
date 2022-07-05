'''
Найти сумму имеющихся в нем цифр
'''
a = int(input("Number? ")
b = a // 100
c = (a % 100) // 10
d = a % 10
if (a > 10) & (a < 100):
  print(c + b)
else: 
  print(b + c + d)
