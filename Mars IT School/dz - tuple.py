'''
#1,3
a = input()
b = a.split()
c = tuple(b)
print(c)


#5
a = ('olma', 'banan', 'apelsin', 'gilos')
print(a + ('dargonmeva',))
     
#6
a = ('olma', 'banan', 'apelsin', 'gilos')
print(a[::-1])


#7
tuple1=("Sariq", [10,20,30],(5,15,25))
print(tuple1[1][1])

#8
tuple1=(11,22)
tuple2=(99,88)
tuple2 =  (11,22)  
tuple1 = (99,88) 
print(tuple1)
print(tuple2)


#9
a = [1, 2, 3, 1, 2, 3]
i = 1
b = []
for i in range(len(a)):
    for e in a:
        if a[i] == e:
            b.append(a[i])
        else:
            continue
print(b)

#10
tuple1 = (11, [22, 33], 44, 55)
a = list(tuple1)
a[1][0] = 222
tuple1 = tuple(a)
print(tuple1)
'''
#13
a = [50, 10, 60, 70, 50]
i = 0
b = []
c = 0
for i in range(len(a)):
    for e in a:
        if a[i] == e:
            c = c + 1
        else:
            continue
print(c)

#14
mashinalar=("Lamborghini", "Bugatti", "Chevrolet")
print(mashinalar[-1])
#15
telefon=("Apple", "Xiaomi", "Oppo")
a = list(telefon)
b =a * 3
telefon = tuple(b)
