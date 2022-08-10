'''
a = {'olma', 'banan', 'shaftoli', 'apelsin'}
b = {'olma', 'banan', 'gilos'}
a.add(123)
print(a)
a.discard('olma')
print(a)
c = a.intersection(b)
print(c)
a.update(b)
print(a)
'''
'''
a = {10, 20, 30, 40, 50}
a.remove(10)
a.discard(20)
del 30 in a
print(a)
'''
'''
a = {'olma', 'banan', 'shaftoli', 'apelsin'}
b = {'olma', 'banan', 'gilos'}
c = a.symmetric_difference(b)
print(c)
'''
'''
a = {10,25,-7,86,999,1,68}
b = list(a)
print(max(a))
print(min(a))
print(b.sort())
for i in a:
    b.append(i ** 2)
c = set(b)
print(c)
'''
'''
set1 = {23, 2, 4, 7, 10}
b = []
c = []
for i in set1:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)
b = set(b)
c = set(c)
print(b)
'''
