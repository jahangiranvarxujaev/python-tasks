'''
даны две строки. Вывести большую по длине строку столько раз,
на сколько символов отличаются строки.
'''
a = input("Firs Word? "))
b = input("Second Word? ")
c = len(a)
d = len(b)
if c > d:
  print(a * (c - d))
else:
  print(b * (d - c))
