a = [12, 'sdsdd', 678, 'dsd']
print(a)
b = input('What do you want to discard? ')
if b.isdigit():
    if int(b) in a:
        a.remove(int(b))
else:
    a.remove(b)
print(a)
